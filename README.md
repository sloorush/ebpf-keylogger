# eBPF Keylogger

Keylogger written in [eBPF](https://ebpf.io/).

## How to run

```sh=
❯ sudo ./ebpf-keylogger -h
usage: bpf-keylogger [-h] [--debug] [-t] [-o OUTFILE] [-u]

A keylogger written in eBPF.

optional arguments:
  -h, --help            show this help message and exit
  --debug               Print debugging info.
  -t, --timestamp       Print time stamps.
  -o OUTFILE, --outfile OUTFILE
                        Output trace to a file instead of stdout.
  -u, --upload          upload the files to google drive
```

## Helpful cmds

```sh=
# To get help
sudo ./ebpf-keylogger -h

# To get the logs in std out run
sudo ./ebpf-keylogger


# You might have to give it executable permission
chmod +x ./ebpf-keylogger


# To get the logs in an outfile
sudo ./ebpf-keylogger -o OUTFILE.txt


# To run it with timestamps,
sudo ./ebpf-keylogger -o OUTFILE.txt -t

# To run it with uploads to google drive
sudo ./ebpf-keylogger -o OUTFILE.txt -t -u
```

Requires:

- The latest version of [bcc](https://github.com/iovisor/bcc)

# Disclaimer

**This code is made for EDUCATIONAL PURPOSES ONLY. We are not liable for any damages**
