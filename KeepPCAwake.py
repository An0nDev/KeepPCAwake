import ctypes, threading

ES_CONTINUOUS        = 0x80000000
ES_SYSTEM_REQUIRED   = 0x00000001

# CONTINUOUS repeats the action until the application closes,
# SYSTEM_REQUIRED 'forces the system to be in the working state by resetting the system idle timer.'
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

try:
    threading.Event ().wait () # infinite non-busy-wait
except KeyboardInterrupt: # catch a Ctrl-C
    pass # do nothing
