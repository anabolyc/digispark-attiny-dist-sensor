## digispark-attiny-dist-sensor

### Hardware

Digispark Attiny85 board with Micronucleos core
Flash included ino file
Distance sensor included

### Software
When object is present in front of sensor - display is swithed on. When object moved away - display is switched off.

## Prerequisites

### Windows
1. driver included
1. python 2.7
1. pip install pyusb
1. pip install pypiwin32

### Ubuntu
1. pip install pyusb
1. add following line to /etc/udev/rules.d/49-micronucleus.rules (create file if necessary)
```
SUBSYSTEMS=="usb", ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="05df", MODE:="0666"
```

## Run
```
python read.py
```