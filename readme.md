# Joey Brute Forcer

A python script that checks every possible combination of update keys for the joey

## Requirements

- Python (Windows users don't need this)
- Crunch (Linux users can install this trough their package manager, Windows users can use the linux subsystem or alternatively try https://github.com/shadwork/Windows-Crunch/releases)

## Usage

Generate the wordlist (Warning this will take up 36GB)
```
crunch 8 8 0123456789abcdef -o JoeyList.txt 
```

Put Joeybruteforcer.exe(Or the .py file if you're on linux) in the same folder as JoeyList.txt and run it

Now wait, the brute forcer will test every possible combination of keys until it finds one that works, it will then output that key to a file named "key.txt"