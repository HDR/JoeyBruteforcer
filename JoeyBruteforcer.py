import string
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x046d, idProduct=0x1234)
with open("JoeyList.txt") as f:
    for line in f:
        B1=int(line[0:2],16).to_bytes(1,'little')
        B2=int(line[2:4],16).to_bytes(1,'little')
        B3=int(line[4:6],16).to_bytes(1,'little')
        B4=int(line[6:8],16).to_bytes(1,'little')
        dev.write(0x01,b'\x81'+B1+B2+B3+B4)
        dev.write(0x01,[0x84])
        if(dev.read(0x81,64)[0] == 1):
            print("Key Found, Outputting to key.txt")
            print(line)
            keyFile = open("key.txt", "w+")
            keyFile.write(line)
            keyFile.close()
            break