# simple python test program.
# This one does no screen updates.
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

l=0
s=""
#this is a dummy function, where we don't actually refresh the screen to see what CPU load there is.
def draw_frame(screen):
    for i in range(screen.height):
        for j in range(screen.width):
            s="{}".format(randint(0,255))

def ds(screen):
    global run_limit
    screen.clear()
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



