from datetime import datetime
import os

from config import CONSOLE_OUTPUT_ON, LOGGING_ENABLED, LOG_DIRECTORY_PATH

def write_to_log(message):
    datestamp = datetime.now().strftime("%m-%y")
    timestamp = datetime.now().strftime("%m/%d/%y [%H:%M:%S]")

    fname = f"log-{datestamp}.txt"

    path_str = f"{LOG_DIRECTORY_PATH}"

    if os.path.exists(path_str) == False:
        os.mkdir(path_str)

    os.chdir(path_str)
    if os.path.exists(fname):
        fout = open(fname, 'a')
        fout.write(f"{timestamp}:    ")
        fout.write(f"{message}\n\n")
    else:
        fout = open(fname, 'w')
        fout.write(f"{timestamp}:    ")
        fout.write(f"{message}\n\n")

def console_and_log(message=""):
    if CONSOLE_OUTPUT_ON:
        print(message)

    if LOGGING_ENABLED:
        write_to_log(message)

def log_last_turn(message):
    fname = "lastturn.txt"
    fout = open(fname, 'w')
    fout.write(message)
    fout.close()


def get_last_turn():
    fname = "lastturn.txt"
    if os.path.exists(fname):
        fout = open(fname, 'r')
        child = fout.readline()
    
    else:
        child = " No File Found. "

    return child