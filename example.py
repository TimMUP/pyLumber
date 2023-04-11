import pylumber as lum


mainLog = lum.lumberjack('test.log')

mainLog.jack("Hello World!", "OK")
mainLog.jack("Hello World!", "ERROR")
mainLog.jack("Hello World!", "DEBUG")


testParameter = [
    ("RED", lum.ANSI_FORE.ACCENT1),
    ("GREEN", lum.ANSI_FORE.ACCENT2),
    ("ORANGE", lum.ANSI_FORE.ACCENT3),
]

testLog = lum.lumberjack('test2.log', logParameter=testParameter)
testLog.jack("Works?", "RED")
testLog.jack("Works?", "GREEN")
testLog.jack("Works?", "ORANGE")

testLog.jack(testLog.format("Works?", "RED"), "RED")
