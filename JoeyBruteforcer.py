import string
import usb.core

dev = usb.core.find(idVendor=0x046d, idProduct=0x1234)
with open("JoeyList.txt") as f:
    for line in f:
        B=int(line[0:8],16).to_bytes(4,'big')
        dev.write(0x01,b'\x81'+B)
        dev.write(0x01,[0x84])
        if(dev.read(0x81,64)[0] == 1):
            print("Key Found, Outputting to key.txt")
            print(line)
            keyFile = open("key.txt", "w+")
            keyFile.write(line)
            keyFile.close()
            break