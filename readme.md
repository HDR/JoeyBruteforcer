# Joey Brute Forcer

A python script that checks every possible combination of update keys for the Joey Joebags (Gen 3)

![](https://i.gyazo.com/bbdd483fe5b5b68ac6b06fbd916a379d.gif)

## Requirements

- Python
- Crunch (Linux users can install this trough their package manager, Windows users can use the linux subsystem or alternatively try https://github.com/shadwork/Windows-Crunch/releases)
- libusb
- pyusb

## Usage

Generate the wordlist (Warning this will take up 36GB)
```
crunch 8 8 0123456789abcdef -o JoeyList.txt 
```

Plug in your Joey (you need to have the drivers installed)

Put Joeybruteforcer.py in the same folder as JoeyList.txt and run it

Now wait, the brute forcer will test every possible combination of keys until it finds one that works, it will then output that key to a file named "key.txt"
