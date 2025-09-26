#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: pkandasamy7

import subprocess
#using def, and  adding the subprocess command
def free_space():
    # Launch: df -h | grep '/$' | awk '{print $4}'
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    out, err = p.communicate()
    # Return UTF-8 string with newline(s) stripped
    return out.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
