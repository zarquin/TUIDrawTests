#run the tests
# then print the results.
"""
TUIDrawTests
Benchmarking for Terminal Drawing 
zarquin@ucc.asn.au
(c) 2020
See LICENSE for licence details
"""

import sh
import subprocess
import time
import datetime
import os, sys
import pprint


global_results={}

#taken from http://granitosaurus.rocks/getting-terminal-size.html
def get_terminal_size(fallback=(80, 24)):
    for i in range(0,3):
        try:
            columns, rows = os.get_terminal_size(i)
        except OSError:
            continue
        break
    else:  # set default if the loop completes which means all failed
        columns, rows = fallback
    return columns, rows

def plain_python_bg_draw_test(cycles=40):

    start_time = datetime.datetime.now()
    cmd = subprocess.run(['python3', 'plain-python-bg-draw.py', str(cycles)])
    time_delta = datetime.datetime.now() - start_time
    return time_delta.total_seconds()  

def numpy_randints_bg_draw_test(cycles=40):
    start_time = datetime.datetime.now()
    cmd = subprocess.run(['python3', 'numpy-randints-bg-draw.py', str(cycles)])
    time_delta = datetime.datetime.now() - start_time
    return time_delta.total_seconds()  

def main():

    global_results["testing start time"] = datetime.datetime.now().strftime("%Y%M%D-%H%M%S")
    (global_results["term_cols"], global_results["term_rows"]) = get_terminal_size()

    # get the time for different test runs.
    global_results["plain_python_bg_draw_test_40_time"]=plain_python_bg_draw_test(cycles=40)
    global_results["plain_python_bg_draw_test_80_time"]=plain_python_bg_draw_test(cycles=80)
    global_results["plain_python_bg_draw_test_200_time"]=plain_python_bg_draw_test(cycles=200)

    #numpy randint tests
    global_results["numpy_randints_bg_draw_test_40_time"]=numpy_randints_bg_draw_test(cycles=40)
    global_results["numpy_randints_bg_draw_test_80_time"]=numpy_randints_bg_draw_test(cycles=80)
    global_results["numpy_randints_bg_draw_test_200_time"]=numpy_randints_bg_draw_test(cycles=200)




    global_results["testing end time"] = datetime.datetime.now().strftime("%Y%M%D-%H%M%S")

    #print("{}".format( global_results))
    pprint.pprint(global_results)


if __name__ == "__main__":
    main()