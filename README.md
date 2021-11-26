# eBPF Keylogger

Keylogger written in [eBPF](https://ebpf.io/).

```sh=
# To get the logs in std out run
sudo ./ebpf-keylogger


# You might have to give it executable permission
chmod +x ./ebpf-keylogger


# To get the logs in an outfile
sudo ./ebpf-keylogger -o OUTFILE


# To run it with timestamps,
sudo ./ebpf-keylogger -o OUTFILE -t
```

Requires:

- The latest version of [bcc](https://github.com/iovisor/bcc)

# Disclaimer

**This code is made for EDUCATIONAL PURPOSES ONLY. We are not liable for any damages**
