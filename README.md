# TUIDrawTests
 Testing Terminal draw speeds

## Background 
 ASCII-Simple-Video-Synth has performance issues when being run on a RaspberryPi, which doesn't quite make sense.
 
 Running Python3 on a RaspberryPi 3 gave a frame rate of only 3-5 FPS when running with a 80x25 window.

 This project is a test suite of different screen drawing techniques and benchmarking them.  
 It will also be useful for understanding the different terminal emulator performances.

## Description

The test suit is a collection of test programs.  Each test program does the same function, just with different techniques.

Each test program draws a sequence of full screens, with each charachter a random colour.  Either setting the background or drawing a foreground character.

The test program takes an argument for how many full screens it should draw, so it can be timed.

## Usage

Usage currently is very simple.  First install the dependancies.

```
pip3 install asciimatics sh
```

Then run:
```
python3 run-tests.py
```


