import pylumber as lum

mainLog = lum.LUMBERJACK('test.log', 0)

mainLog.pinfo("Hello World!")
