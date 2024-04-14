import time
import os


conf_yaml = "direct_ssh.yaml"


while True:
    # check if there are USB drives mounted
    for usb in [f"/media/usb{i}" for i in range(8)]:
        # check if there is a file called "DIRECT.SSH" to flag the usb drive as a direct ssh prompt
        if not (os.path.isfile(usb + "DIRECT.SSH")):
            # if there is no file, continue with the next usb device
            continue
        # if there is such a file, continue
        # move current netplan .yaml to a safe copy
    os.renam(os.list("/etc/netplan")[0], "")
    time.sleep(2)

