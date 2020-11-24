# OBD-II
Senior Design project. OBD-II to HUD. This is designed to work on a RaspberryPi running raspian.

## Python 
- Requires python 3.X
- Required Packages
	- `$ python3 -m pip install pysimplegui`
	- `$ python3 -m pip install -U matplotlib`
 
## Linux
- Hide Navbar
- Change SCREENX and SCREENY variables in Display.py to match device's resolution
- Configure to run Display.py on boot by moving `OBD-II-HUD.service` to /lib/systemd/system directory
	- `sudo chmod 644 /lib/systemd/system/OBD-II-HUD.service`
	- `sudo systemctl daemon-reload`
	- `sudo systemctl enable OBD-II-HUD.service`

