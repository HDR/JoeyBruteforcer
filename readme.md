# Joey Brute Forcer

A python script that checks every possible combination of update keys for the Joey Joebags (Gen 3)

Estimated max time to crack (8700K) 14-15 Days (4294967296 Lines)

![](https://i.gyazo.com/bbdd483fe5b5b68ac6b06fbd916a379d.gif)

The gif above is an example, the actual script has no output to increase the speed.

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


## Notes

Keys may contain only numbers or letters, using a wordlist that only has one of these before using a bigger one may be benefitial.

Numbers
```
crunch 8 8 0123456789 -o JoeyList.txt 
```

Letters
```
crunch 8 8 abcdef -o JoeyList.txt 
```

If you don't want to run the script for days you can generate the wordlist in chunks and then rename one chunk to "JoeyList.txt" and do it that way
```
crunch 8 8 0123456789abcdef -b 250mb -o START
```
This generates 250mb files, on a modern system (8700k) it takes just over 3 hours to go trough one file
