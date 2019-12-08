import string

import usb.core
import usb.util

dev = usb.core.find(idVendor=0x046d, idProduct=0x1234)
with open("JoeyList.txt") as f:
    for line in f:
        Key=line[0:8]
        B1=int(Key[0:2],16)
        B2=int(Key[2:4],16)
        B3=int(Key[4:6],16)
        B4=int(Key[6:8],16)
        B1=B1.to_bytes(1,'little')
        B2=B2.to_bytes(1,'little')
        B3=B3.to_bytes(1,'little')
        B4=B4.to_bytes(1,'little')
        WriteCommand=b'\x81'+B1+B2+B3+B4
        dev.write(0x01,WriteCommand)
        USBbuffer = dev.read(0x81,64)
        dev.write(0x01,[0x84])
        USBbuffer = dev.read(0x81,64)
        if(USBbuffer[0] == 1):
            print("Key Found, Outputting to key.txt")
            print(line)
            keyFile = open("key.txt", "w+")
            keyFile.write(line)
            keyFile.close()
            break