import pylumber as lum


mainLog = lum.lumberjack('test.log', silent=True)

mainLog.log("Hello World!", "OK")
mainLog.log("Hello World!", "ERROR")
mainLog.log("Hello World!", "DEBUG")


testParameter = [
    ("RED", lum.ANSI_FORE.ACCENT1),
    ("GREEN", lum.ANSI_FORE.ACCENT2),
    ("ORANGE", lum.ANSI_FORE.ACCENT3),
]

testLog = lum.lumberjack('test2.log', logParameter=testParameter)
testLog.log("Works?", "RED")
testLog.log("Works?", "GREEN")
testLog.log("Works?", "ORANGE")

testLog.log(testLog.format("Works?", "RED"), "RED")
