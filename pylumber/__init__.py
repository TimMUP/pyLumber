# ~~~~~~ |
# pyLumber.py - Lumberjack for your Code, Logs, Prints, 
# Errors and more.
# Author: Tim Yang (TimMUP)
# Editor:
# Status: In Development MIT License
# Version: 0.0.1
# Date: 2019-01-01
# ~~~~~~ |

import os
import timeit


class ANSI_MODI:
    """ANSI Modification Codes"""
    BOLD        = '\033[1m'             # BOLD
    UNDERLINE   = '\033[4m'             # UNDERLINE
    BLINK       = '\033[5m'             # BLINK
    REVERSE     = '\033[7m'             # REVERSE
    CONCEALED   = '\033[8m'             # CONCEALED
    END         = '\033[0m'             # DEFAULT

class ANSI_FORE:
    """ANSI Foreground Color Codes"""
    ACCENT1     = '\033[91m'            # RED
    ACCENT2     = '\033[92m'            # GREEN
    ACCENT3     = '\033[93m'            # YELLOW
    ACCENT4     = '\033[94m'            # BLUE
    ACCENT5     = '\033[95m'            # MAGENTA
    ACCENT6     = '\033[96m'            # CYAN
    
class ANSI_BACK:
    """ANSI Background Color Codes"""
    ACCENT1     = '\033[101m'            # RED
    ACCENT2     = '\033[102m'            # GREEN
    ACCENT3     = '\033[103m'            # YELLOW
    ACCENT4     = '\033[104m'            # BLUE
    ACCENT5     = '\033[105m'            # MAGENTA
    ACCENT6     = '\033[106m'            # CYAN


#class HEADER:
#    INFO = COLOR


def test(msg, ansi):
    print("%s%s%s" %(ansi, msg, ANSI_MODI.END))


class LUMBERJACK:
    def __init__(self, logFile=None, logLevel=0):
        self.logFile = open(logFile, "w") if logFile else None
    
    def 

# PRINT Information Prompt and Saves to Log File


test("Hello World", ANSI_FORE.ACCENT1)
