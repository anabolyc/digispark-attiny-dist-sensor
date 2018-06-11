#/usr/bin/python

#
# Written for PyUSB 1.0 (w/libusb 1.0.3)

import usb # 1.0 not 0.4
import os
import sys
sys.path.append("..")


from arduino.usbdevice import ArduinoUsbDevice
from subprocess import call

WIN_SCREEN_ON = -1
WIN_SCREEN_SLEEP = 1
WIN_SCREEN_OFF = 2
WIN_SC_MONITORPOWER = 0xF170

def screen_state_win(state):
    import win32gui
    import win32con
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, WIN_SC_MONITORPOWER, state)   

def screen_on():
    sys.stdout.write(" ON")
    if sys.platform.startswith('linux'):
        os.system("xset dpms force on")
    elif sys.platform.startswith('win'):
        screen_state_win(WIN_SCREEN_ON)

def screen_off():
    sys.stdout.write(" OFF")
    if sys.platform.startswith('linux'):
        os.system("xset dpms force off")
    elif sys.platform.startswith('win'):
        screen_state_win(WIN_SCREEN_OFF)
    #elif sys.platform.startswith('darwin'):
    #    import subprocess
    #    subprocess.call('echo \'tell application "Finder" to sleep\' | osascript', shell=True)

if __name__ == "__main__":
    try:
        theDevice = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)

        print "Found: 0x%04x 0x%04x %s %s" % (theDevice.idVendor, 
                                              theDevice.idProduct,
                                              theDevice.productName,
                                              theDevice.manufacturer)
    except:
        pass

    import sys
    import time

    CMD_ON  = "a2ce4f368c4b"
    CMD_OFF = "67faacf02530"

    msg = ""
    while 1 == 1:
        try:
            theDevice = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)
            try:
                c = chr(theDevice.read())

                if c == '\0':
                    sys.stdout.write(msg)
                    
                    if msg == CMD_ON:
                        screen_on()
                    
                    if msg == CMD_OFF:
                        screen_off()

                    sys.stdout.write("\n")
                    msg = ""
                else:
                    msg += c    

                sys.stdout.flush()
            except:
                time.sleep(0.1)
                
        except:
            time.sleep(0.25)
            
       
        
