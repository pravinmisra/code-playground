# -*- coding: utf-8 -*-
"""
Created on Fri May 30 19:32:49 2025

@author: Admin
"""

import sys, time
import sevseg  # Imports our sevseg.py program.

# (!) Change this to any number of seconds:
secondsLeft = 30

try:
    while True:
        # Main program loop.
    
        # Clear the screen by printing several newlines:
        print('\n' * 60)
 
        hours = str(secondsLeft // 3600)
        
        minutes = str((secondsLeft % 3600) // 60)
        
        seconds = str(secondsLeft % 60)
 
        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines() 
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
 
        # Display the digits:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
 
        if secondsLeft == 0:
             print()
             print('    * * * * BOOM * * * *')
             break
 
        print()
        print('Press Ctrl-C to quit.')
 
        time.sleep(1)  # Insert a one-second pause.
        secondsLeft -= 1
except KeyboardInterrupt:
        print('Countdown, by Pravin Misra')
        sys.exit()  # When Ctrl-C is pressed, end the program.)