import os
import sys
import pathlib
import subprocess


if not os.getuid() == 0:
    print("MUST BE RUN AS ROOT USER")
    sys.exit(1)


input('The GitHub Repo "rbrito/usbmount" is required to use this script. please install it first. For Instructions see "README.md"\n(Press ENTER to continue...)')


path = pathlib.Path(__file__).parent.resolve()


# setup service
print("setting up service...")
with open("DIRECT_SSH.service", "w") as f:
    f.write("[Unit]" + "\n")
    f.write("Description=Auto run direct-ssh/server.py" + "\n")
    f.write("After network.target=auditd.service" + "\n")
    f.write("" + "\n")
    f.write("[Service]" + "\n")
    f.write("User=root" + "\n")
    f.write(f"WorkingDirectory={path}" + "\n")
    f.write(f"ExecStart=/usr/bin/python3 {path}/main.py" + "\n")
    f.write("" + "\n")
    f.write("[Install]" + "\n")
    f.write("WantedBy=multi-user.target" + "\n")

os.rename("DIRECT_SSH.service", "/etc/systemd/system/DIRECT_SSH.service")


# reload daemon
print("reloading systemctl daemon...")
subprocess.run(["systemctl", "daemon-reload"])

# enable service
print("enabling service...")
subprocess.run(["systemctl", "enable", "DIRECT_SSH.service"])

# restarting services
print("starting service...")
subprocess.run(["systemctl", "restart", "DIRECT_SSH.service"])

print("DONE!")