# TUIDrawTests
 Testing Terminal draw speeds

## Background 
 ASCII-Simple-Video-Synth has performance issues when being run on a RaspberryPi, which don't quite make sense.
 
 Running Python3 on a RaspberryPi 3 gave a frame rate of only 3-5 FPS when running with a 80x25 window.

 This project is a test suite of different screen drawing techniques and benchmarking them, so I can find out where the RaspberryPI slowdowns are.  
 It will also be useful for understanding the different terminal emulator performances.

## Description

The test suit is a collection of test programs.  Each test program does the same function, just with different techniques.

Each test program draws a sequence of full screens, with each charachter a random colour.  Either setting the background or drawing a foreground character.

The test program takes an argument for how many full screens it should draw, so it can be timed.

## Usage

Usage currently is very simple.  First install the python3 dependancies.

```
pip3 install asciimatics sh numpy PyInquirer
```
Then we need to compile the rust code.  If you don't have rust installed.. Install rust:

[Rust's Install page...  https://www.rust-lang.org/tools/install ](https://www.rust-lang.org/tools/install)

Open a terminal in the TUIDrawTests top level.
```
cd rust-crossterm-bg-draw/
cargo run 10
cd ..
```
When you type `cargo run 10` it will download all the rust dependencies, compile the test program, and then run it briefly.

Make sure you're at the top directory of `TUIDrawTests` and then run the tests using:
```
python3 run-tests.py
```

## Understanding the results
The results at the moment are pretty damn simple. At the end of the testing,  you get a console printout with some test parameters, and some testing time results.

Currently, each drawing test is repeated three times with different numbers of frames to draw each time.  These are 40, 80 and 200 times.
This should give some indication about screen refreshing performance.

The drawing tests currently are:

| Test Name | Description |
|:---:|---|
| `numpy_randints_bg_draw_test`| Using Numpy table of random ints that is the size of the screen to set the BG colour.|
|`numpy_randints_bg_paint_test`| Using Numpy table, but using the `paint()` method instead of `print_at()`|
|`plain_python_bg_draw_hirefresh`| Deliberatly slamming the screen drawing by calling `screen.refresh()` after each line|
|`plain_python_bg_draw_test`| A very boring code.  Iterates through every cell on the screen calling `randint()` and then does a refresh at the end.|
|`plain_python_no_draw_test`| Same code as `plain_python_bg_draw_test` except it takes the output of `randint()` to a string instead of calling `print_at()`.  THis should give some indication of CPU performance|
|`rust_crossterm_bg_draw`| The same process as `plain_python_bg_draw_test` except done using rust.  this should show performance differences|






