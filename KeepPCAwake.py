import ctypes

ES_CONTINUOUS        = 0x80000000
ES_SYSTEM_REQUIRED   = 0x00000001

# CONTINUOUS repeats the action until the application closes,
# SYSTEM_REQUIRED 'forces the system to be in the working state by resetting the system idle timer.'
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

# wait until broken
while True:
    # attempt to run the following code
    try:
        # try needs some code as an argument, so I just added a zero.
        0
    except(KeyboardInterrupt): # catch a Ctrl+C
        break # stop waiting