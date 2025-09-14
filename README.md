![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

# Direct-SSH
Direct-SSH is a lightweight script that runs when a USB drive is connected with a single file called `DIRECT.SSH`. The script will then change the Netplan settings, so that the Raspberry Pi is assigned the static IP address `192.168.0.50` on eth0. When the USB drive is disconnected, the netplan is automatically reverted to its original configuration.

The script can come in handy if you are in a networkless environment but still need to SSH into your Raspberry Pi.

## Prerequisites
- Raspberry Pi running Ubuntu Server 22.04.3 LTS or similar
- Internet access for initial setup
- GitHub CLI (`gh`) installed

## Installation of USBMOUNT
Install Rbrito's usbmount:
```bash
apt-get install -y debhelper build-essential
gh repo clone rbrito/usbmount
cd usbmount
dpkg-buildpackage -us -uc -b
sudo dpkg -i ../usbmount_*.deb
rm ../usbmount_*  # Clean up build files
cd ../direct-ssh
```
For further instructions visit [Rbrito`s Repo](https://github.com/rbrito/usbmount)

Automated installation of systemd service:
```bash
sudo python3 setup.py
```

## Usage
### Connecting Direct-SSH
1. Create an empty file called `DIRECT.SSH` on a USB thumbdrive. The file should be the only file on that USB drive.
2. Plug the USB drive into the Raspberry Pi
3. After a few seconds the netplan will be reconfigured to set the static IP address `192.168.0.50` on the interface `eth0`
4. Connect your Raspberry Pi directly to your computer using an Ethernet cable
5. Open a console and SSH into your Raspberry Pi using the IP address `192.168.0.50`
6. You now have a direct SSH connection established.

### Disconnecting Direct-SSH
1. Disconnect the USB drive that contains the file `DIRECT.SSH`
2. The script will automatically revert the Netplan configuration to its original state.

## Tested environments
Direct-SSH has been tested in the following environments. Compatibility with other hardware or operating systems has not yet been verified.

* Raspberry Pi 3B running Ubuntu server 22.04.3 LTS
* Raspberry Pi 4B running Ubuntu server 22.04.3 LTS
* Raspberry Pi 5B running Ubuntu server 22.04.3 LTS

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
