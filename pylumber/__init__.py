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
import re
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

class CONST:
    PREFIX_SPACE = 8
    PREFIX_CHAR = " "
    PREFIX_MODI = [ANSI_MODI.BOLD]

class LOG_PREFIX:
    # List of Modifications for Prefixes
    INFO_MODI   = [ANSI_FORE.ACCENT4]
    INFO        = "%s[%s]%s" %(''.join(CONST.PREFIX_MODI + INFO_MODI),
                               "INFO".center(CONST.PREFIX_SPACE, CONST.PREFIX_CHAR),
                               ANSI_MODI.END)
    OK_MODI     = [ANSI_FORE.ACCENT2]     
    OK          = "%s[%s]%s" %(''.join(CONST.PREFIX_MODI + OK_MODI),
                              "OK".center(CONST.PREFIX_SPACE, CONST.PREFIX_CHAR), 
                              ANSI_MODI.END)
    WARN_MODI   = [ANSI_FORE.ACCENT3]
    WARN        = "%s[%s]%s" %(''.join(CONST.PREFIX_MODI + WARN_MODI), 
                              "WARN".center(CONST.PREFIX_SPACE, CONST.PREFIX_CHAR), 
                              ANSI_MODI.END)
    ERROR_MODI  = [ANSI_FORE.ACCENT1]
    ERROR       = "%s[%s]%s" %(''.join(CONST.PREFIX_MODI + ERROR_MODI), 
                              "ERROR".center(CONST.PREFIX_SPACE, CONST.PREFIX_CHAR), 
                              ANSI_MODI.END)
    DEBUG_MODI  = [ANSI_FORE.ACCENT5]
    DEBUG       = "%s[%s]%s" %(''.join(CONST.PREFIX_MODI + DEBUG_MODI), 
                               "DEBUG".center(CONST.PREFIX_SPACE, CONST.PREFIX_CHAR), 
                               ANSI_MODI.END)

# q: What is the regex expression for matching all sets between '\' and 'm'?
# a: \033\[[0-9;]*m

# Helper Function | Removes all ANSI Codes from String
def STRIP_ANSI(string):
    return re.sub(r'\033\[[0-9;]*m', '', string)

class LUMBERJACK:
    def __init__(self, logFile=None, logLevel=0):
        self.logFile = open(logFile, "w") if logFile else None
    
    def pinfo(self, msg):
        print(f"{LOG_PREFIX.INFO} {msg}")
        if self.logFile:
            self.logFile.write(STRIP_ANSI(f"{LOG_PREFIX.INFO} {msg}"))

    def pok(self, msg):
        print(f"{LOG_PREFIX.OK} {msg}")
        if self.logFile:
            self.logFile.write(STRIP_ANSI(f"{LOG_PREFIX.OK} {msg}"))

    def pwarn(self, msg):
        print(f"{LOG_PREFIX.WARN} {msg}")
        if self.logFile:
            self.logFile.write(STRIP_ANSI(f"{LOG_PREFIX.WARN} {msg}"))

    def pdebug(self, msg):
        print(f"{LOG_PREFIX.DEBUG} {msg}")
        if self.logFile:
            self.logFile.write(STRIP_ANSI(f"{LOG_PREFIX.DEBUG} {msg}"))

    def perror(self, msg):
        print(f"{LOG_PREFIX.ERROR} {msg}")
        if self.logFile:
            self.logFile.write(STRIP_ANSI(f"{LOG_PREFIX.ERROR} {msg}"))

# PRINT Information Prompt and Saves to Log File

testJacker = LUMBERJACK(logFile="test.log")
testJacker.pinfo("Hello World")
testJacker.pok("Hello World")
testJacker.pwarn("Hello World")
testJacker.perror("Hello World")
testJacker.pdebug("Hello World")
