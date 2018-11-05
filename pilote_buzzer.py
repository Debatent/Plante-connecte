"""
MIT License

Copyright (c) 2018 Debatent and GuillaumeClementPolytech

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, subject 
to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import time
import grovepi


def sonnerie_buzzer (num_pin_buzzer):
    grovepi.pinMode(num_pin_buzzer,"OUTPUT")
    
    # Buzz for 0.5 second
    grovepi.digitalWrite(num_pin_buzzer,1)
    print ('on')
    time.sleep(0.5)
    
    # Stop buzzing for 5 minute and repeat
    grovepi.digitalWrite(num_pin_buzzer,0)
    print ('off')
    time.sleep(300)