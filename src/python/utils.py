import os, sys

# Execute a function with dropped privileges (if we have privileges to drop)
def drop_privileges(func):
    def inner(*args, **kwargs):
        try:
            sudo_uid = os.environ["SUDO_UID"]
            sudo_gid = os.environ["SUDO_GID"]

            # Remember current euid and egid
            euid = os.geteuid()
            egid = os.getegid()

            # Drop privileges
            os.setegid(int(sudo_gid))
            os.seteuid(int(sudo_uid))

            # Call wrapped function
            ret = func(*args, **kwargs)

            # Restore privileges
            os.setegid(egid)
            os.seteuid(euid)

            return ret

        except KeyError:
            print(
                "WARNING: Unable to drop privileges. Are you running as root?",
                file=sys.stderr,
            )
            return func(*args, **kwargs)

    return inner
