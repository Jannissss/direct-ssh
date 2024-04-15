# direct-ssh

Direct-SSH is a simple script that runs when a USB drive is connected with a single file called `DIRECT.SSH` The Script will then change the Netplan settings, so that the Raspberry Pi has the static address `192.168.0.50` on eth0. When the USB drive is disconnected, the netplan is automatically reverted to its original configuration.

The script can come in handy if you are in a networkless environment but still need to SSH into your Raspberry Pi.

## Installation of USBMOUNT
USBMOUNT is a simple service that automatically mounts USB drives when connected. This is needed for the script to finde the `DIRECT.SSH` file on connected USB drives.

1. `gh repo clone rbrito/usbmount`
2. `cd usbmount`
3. `dpkg-buildpackage -us -uc -b`
4. `sudo dpkg -i ../____.deb`

## Installation of Systemd service

1. `sudo python3 setup.py`

## Usage

### Connecting Direct-SSH

1. Create a file called `DIRECT.SSH` on a USB thumbdrive. The file should be the only file on that USB drive.
2. Plug in the USB drive into the Raspberry Pi
3. After a few seconds the netplan will be reconfigured to set the static IP address `192.168.0.50` on the interface `eth0`
4. Connect to your Raspberry Pi directly via an ethernet cable to your device
5. Open a console and ssh into your Raspberry Pi with the IP address `192.168.0.50`
6. Done! Now you have a direct SSH connection established!

### Disconnecting Direct-SSH

1. Disconnect the USB drive that contains the file `DIRECT.SSH`
2. It's as easy as that! Now the script will automatically revert all changes done to your netplan and reapply it.

## Tested environments

Direct-SSH has not yet been thoroughly tested under different circumstances. This are the specifications that Direct-SSH has been tested in yet:

* Raspberry Pi 3B running Ubuntu server 22.04.4 LTS

## Requirements

1. Python >= 3.10
    * See [Python.org](https://wiki.python.org/moin/BeginnersGuide)
2. debhelper
    * `apt-get install -y debhelper`
3. build-essential
    * `apt-get install -y build-essential`
