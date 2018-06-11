## digispark-attiny-dist-sensor

WIP

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