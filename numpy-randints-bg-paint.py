#numpy draw test
"""
TUIDrawTests
Benchmarking for Terminal Drawing 
zarquin@ucc.asn.au
(c) 2020
See LICENSE for licence details
"""
import numpy as np
from asciimatics.screen import Screen
import argparse

run_limit=0

def draw_frame(screen):
    array=np.random.randint(256, size=(screen.height, screen.width))
    array_fg=np.full((3,screen.width),0)  # set the array to make to a tuple

    for i in range(screen.height):
        sttr = " "*screen.width
        array_line = array[i]
        array_fg[2] = array_line   #want to replace the 3rd row
        ff = list(map(tuple,np.rot90(array_fg)))
        screen.paint(sttr, 0,i,colour_map=ff )
    screen.refresh()

def ds(screen):
    global run_limit
    while run_limit > 0:
        draw_frame(screen)
        run_limit=run_limit-1

def main():
    global run_limit
    parser = argparse.ArgumentParser()
    parser.add_argument("runframes", type=int, default = 10, help="a fixed amount of frames to run for")
    args = parser.parse_args()
    run_limit = args.runframes

    Screen.wrapper(ds)
    exit()

if __name__ == "__main__":
    main()
