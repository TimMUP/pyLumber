import pylumber as lum


mainLog = lum.LUMBERJACK('test.log')

mainLog.jack("Hello World!", "OK")
mainLog.jack("Hello World!", "ERROR")
mainLog.jack("Hello World!", "DEBUG")


testParameter = [
    ("TEST", lum.ANSI_FORE.ACCENT1),
    ("TEST2", lum.ANSI_FORE.ACCENT2),
    ("TEST3", lum.ANSI_FORE.ACCENT3),
]
testLog = lum.LUMBERJACK('test2.log', logParameter=testParameter)
testLog.jack("Works?", "TEST")
