# Installing Ubuntu
## prerequisites
You will need:

- Spare USB drive with at least 8 gigabytes
  - If you don't have this, you can ask alec, ryan, or tuyet (thats me!) to do it for you
- A laptop with:
	- at least 16 gigabytes of ram
	- a port to connect your USB drive into

## installation
1. Download [Ventoy](https://www.ventoy.net/en/download.html) on your USB drive
	- Linux users: install the .tar.gz file and run `tar -xvf {.tar.gz file here}` to extract the file contents
	- Windows users: install and extract the .zip file
2. Install the desktop version of [Ubuntu 22.04](https://releases.ubuntu.com/jammy/)
3. Move the .iso file to the usb drive
4. Boot into the BIOS and Disable Secure Boot
	1.  Restart your laptop and mash the F10, F11, and F12 buttons to boot into your BIOS
	2. Turn secure boot off (will probably be in the boot menu)
5. Boot into your USB drive and select the iso file
6. Follow the installation process and DO NOT TURN OFF YOUR LAPTOP
7. after the installation, reboot into your BIOS and enable Secure Boot

## partitioning
if you are completely removing windows and switching to ubuntu, you can just select the "wipe hard drive" option. ubuntu will automatically partition your hard drive for you
