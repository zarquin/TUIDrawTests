#run the tests
# then print the results.
"""
TUIDrawTests
Benchmarking for Terminal Drawing 
zarquin@ucc.asn.au
(c) 2020
See LICENSE for licence details
"""
from __future__ import print_function, unicode_literals
from PyInquirer import prompt

import sh
import subprocess
import time
import datetime
import os, sys
import pprint
import platform
import json

global_results={}

def get_platform_info():
    a = platform.platform()
    b = platform.system()
    c = platform.version()
    d = platform.release()
    return a.replace(" ","_")

def get_test_notes():
    questions = [
    {
        'type': 'input',
        'name': 'notes',
        'message': 'Any Notes about this test',
     }]
    return prompt(questions)

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

#taken from https://unix.stackexchange.com/questions/264329/get-the-terminal-emulator-name-inside-the-shell-script
def get_terminal_emulator_name():
    shell_pid = os.getppid()
    term_em="unknown"
    try:
        #get the parent of the shell
        term_em_pid = sh.ps('-o','ppid=','-p',shell_pid).strip()
        term_em_name = sh.ps('-o','comm=','-p',term_em_pid)
        term_em = term_em_name.strip()
    except Exception:
       term_em="unknown"
    return term_em
#
# Tests to run are listed below here.  they return the elapsed run time.  they taken an argument of how many full screen cycles to run.
#

# Rust based version
def rust_crossterm_bg_draw_test(cycles=40):
    start_time = datetime.datetime.now()
    cmd = subprocess.run(['rust-crossterm-bg-draw/target/debug/rust-crossterm-bg-draw',str(cycles)])
    time_delta = datetime.datetime.now() - start_time
    return time_delta.total_seconds()

# No Draw test, to see what CPU load there is and what impact the screen drawing has.
def plain_python_no_draw_test(cycles=40):
    start_time = datetime.datetime.now()
    cmd = subprocess.run(['python3','plain-python-no-draw.py',str(cycles)])
    time_delta = datetime.datetime.now() - start_time
    return time_delta.total_seconds()

def plain_python_bg_hirefresh_test(cycles=40):
    start_time = datetime.datetime.now()
    cmd = subprocess.run(['python3', 'plain-python-bg-draw-hirefresh.py', str(cycles)])
    time_delta = datetime.datetime.now() - start_time
    return time_delta.total_seconds()      

def plain_python_bg_draw_test(cycles=40):
    start_time = datetime.datetime.now()
    cmd = subprocess.run(['python3', 'plain-python-bg-draw.py', str(cycles)])
    time_delta = datetime.datetime.now() - start_time
    return time_delta.total_seconds()  

def numpy_randints_bg_paint_test(cycles=40):
    start_time = datetime.datetime.now()
    cmd = subprocess.run(['python3', 'numpy-randints-bg-paint.py', str(cycles)])
    time_delta = datetime.datetime.now() - start_time
    return time_delta.total_seconds() 

def numpy_randints_bg_draw_test(cycles=40):
    start_time = datetime.datetime.now()
    cmd = subprocess.run(['python3', 'numpy-randints-bg-draw.py', str(cycles)])
    time_delta = datetime.datetime.now() - start_time
    return time_delta.total_seconds()  

def main():
    #get some starting test data.

    global_results["notes"] = get_test_notes()['notes']
    global_results["testing_start_time"] = datetime.datetime.now().strftime("%Y%M%D-%H%M%S")
    global_results["testing_platform"] = get_platform_info()
    (global_results["term_cols"], global_results["term_rows"]) = get_terminal_size()
    global_results["term_name"] = get_terminal_emulator_name()

    # do a run of the no-screen-draw option.
    global_results["plain_python_no_draw_test_40_time"]=plain_python_no_draw_test(cycles=40)
    global_results["plain_python_no_draw_test_80_time"]=plain_python_no_draw_test(cycles=80)
    global_results["plain_python_no_draw_test_200_time"]=plain_python_no_draw_test(cycles=200)

    # get the time for different test runs.
    global_results["plain_python_bg_draw_test_40_time"]=plain_python_bg_draw_test(cycles=40)
    global_results["plain_python_bg_draw_test_80_time"]=plain_python_bg_draw_test(cycles=80)
    global_results["plain_python_bg_draw_test_200_time"]=plain_python_bg_draw_test(cycles=200)

    # high refresh version. does a refresh at the end of each line.
    global_results["plain_python_bg_draw_hirefresh_40_time"]=plain_python_bg_hirefresh_test(cycles=40)
    global_results["plain_python_bg_draw_hirefresh_80_time"]=plain_python_bg_hirefresh_test(cycles=80)
    global_results["plain_python_bg_draw_hirefresh_200_time"]=plain_python_bg_hirefresh_test(cycles=200)

    #numpy randint tests
    global_results["numpy_randints_bg_draw_test_40_time"]=numpy_randints_bg_draw_test(cycles=40)
    global_results["numpy_randints_bg_draw_test_80_time"]=numpy_randints_bg_draw_test(cycles=80)
    global_results["numpy_randints_bg_draw_test_200_time"]=numpy_randints_bg_draw_test(cycles=200)

    #numpy randomint using full line paint method
    global_results["numpy_randints_bg_paint_test_40_time"]=numpy_randints_bg_paint_test(cycles=40)
    global_results["numpy_randints_bg_paint_test_80_time"]=numpy_randints_bg_paint_test(cycles=80)
    global_results["numpy_randints_bg_paint_test_200_time"]=numpy_randints_bg_paint_test(cycles=200)
   
    #rust using corssterm.
    global_results["rust_crossterm_bg_draw_test_40_time"]=rust_crossterm_bg_draw_test(cycles=40)
    global_results["rust_crossterm_bg_draw_test_80_time"]=rust_crossterm_bg_draw_test(cycles=80)
    global_results["rust_crossterm_bg_draw_test_200_time"]=rust_crossterm_bg_draw_test(cycles=200)

    global_results["testing_end_time"] = datetime.datetime.now().strftime("%Y%m%D-%H%M%S")

    x=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    json_filename="Results/result-{}.json".format(x)

    with open(json_filename, 'w') as outfile:
        json.dump(global_results, outfile)

    print("   Testing done    ")

if __name__ == "__main__":
    main()
