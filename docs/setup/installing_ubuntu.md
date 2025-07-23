# Installing Ubuntu 22.04

This guide will help you safely install Ubuntu 22.04 on your laptop for robotics development.

---

## Prerequisites

You will need:

- **USB drive** (at least 8GB)
    - If you don't have a USB, ask Alec, Ryan, or Tuyet.
- **Laptop** with:
    - At least 16GB RAM
    - A USB port

---

## Installation Steps

1. **Prepare the USB Drive**
    - Download [Ventoy](https://www.ventoy.net/en/download.html) and install it on your USB drive.
	 	- Linux: Extract the `.tar.gz` and run `tar -xvf <filename>.tar.gz`.
	 	- Windows: Extract the `.zip` file and run the installer.
2. **Download Ubuntu**
   	- Get the desktop ISO for [Ubuntu 22.04](https://releases.ubuntu.com/jammy/).
3. **Copy the ISO**
   	- Move the downloaded `.iso` file to your Ventoy USB drive.
4. **BIOS Setup**
	- Restart your laptop and enter BIOS (try F10, F11, or F12 during boot).
	- **Disable Secure Boot** (usually in the Boot or Security menu).
5. **Boot from USB**
	- Select your USB drive as the boot device.
	- In Ventoy, choose the Ubuntu ISO to start installation.
6. **Install Ubuntu**
   	- Follow the on-screen instructions. **Do not turn off your laptop during installation!**
7. **Post-Install**
   	- After installation, reboot and re-enable Secure Boot in BIOS if needed.

---

## Partitioning Tips

- If you want to completely replace Windows, select "Erase disk and install Ubuntu" during setup. Ubuntu will handle partitioning automatically.
- For dual-boot setups, choose "Install Ubuntu alongside Windows" and follow the prompts.

---

## Troubleshooting & Safety

- **Backup your data** before starting! Installing Ubuntu will erase your hard drive if you choose the wipe option.
- If you get stuck, check the [official Ubuntu installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop) or ask a team member for help.

---
