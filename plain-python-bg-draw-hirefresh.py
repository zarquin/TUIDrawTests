# simple python test program.  Hammers the screen refresh
"""
TUIDrawTests
Benchmarking for Terminal Drawing 
zarquin@ucc.asn.au
(c) 2020
See LICENSE for licence details
"""

from random import randint
from asciimatics.screen import Screen
import argparse

run_limit=0

def draw_frame(screen):
    for i in range(screen.height):
        for j in range(screen.width):
            screen.print_at(" ",j,i,bg=randint(0, screen.colours - 1))
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