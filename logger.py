from datetime import datetime
import os
from config import CONSOLE_OUTPUT_ON, LOGGING_ENABLED, LOG_DIRECTORY_PATH


def write_to_log(message):
    datestamp = datetime.now().strftime("%m-%y")
    timestamp = datetime.now().strftime("%m/%d/%y [%H:%M:%S]")
    fname = f"log-{datestamp}.txt"
    path_str = LOG_DIRECTORY_PATH

    if not os.path.exists(path_str):
        os.mkdir(path_str)

    os.chdir(path_str)
    with open(fname, 'a' if os.path.exists(fname) else 'w') as fout:
        fout.write(f"{timestamp}:    {message}\n\n")


def console_and_log(message=""):
    if CONSOLE_OUTPUT_ON:
        print(message)
    if LOGGING_ENABLED:
        write_to_log(message)


def log_last_turn(child):
    timestamp = datetime.now().isoformat()
    with open("lastturn.txt", "w") as f:
        f.write(f"{child},{timestamp}")


import os
from datetime import datetime

def get_last_turn():
    if not os.path.exists("lastturn.txt"):
        return "NO_FILE", None

    with open("lastturn.txt", "r") as f:
        lines = f.readlines()

    for line in reversed(lines):
        line = line.strip()
        if not line:
            continue

        child, timestamp = line.split(",", 1)
        child = child.strip()
        if child == "BEN" or "AMELIA":
            return child, datetime.fromisoformat(timestamp.strip())
        else:
            continue
        
    return "READ_ERROR"
            

