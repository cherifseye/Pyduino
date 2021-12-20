'''
CHERIF AHMAD SEYE
PHYSICAL ENGINEERING
SETUX CORPORATION GROUP
2021 - QUEBEC
'''
# NOTICE: TO RUN THJE EXAMPLES, YOU NEED TO 
import main
from time import sleep

pyduino_ = main.pyduino('/dev/cu.usbmodem142301')
print('----------------------------------------------------------------------------------')



if __name__ == '__main__':

    #Example 1: TURN ON A LED
    '''use the __on__() method to turn on a led'''
    '''
    bluePin = 13
    while True:
        pyduino_.__on__(bluePin)
        print('on')
    '''
    
    print('----------------------------------------------------------------------------------')
    #Example 2: BLINK A LED
    '''
    In this example we make the LED blink by calliig the methods __on__ and __off__ 
    The function __on__() will turn on the LED and the function __off__() will turn off the LED
    '''

    '''
    bluePin = 13
    while True:
        pyduino_.__on__(bluePin)
        print('on')
        sleep(1)
        pyduino_.__off__(bluePin)
        print('off')
        sleep(1)
    '''

    print('----------------------------------------------------------------------------------')

    #Example 3: Control 2 LED using a switch button

    '''
    We will make a control panel with a switch and lights turn on when you press the switch
    The green led will be on until the switch is pressed the red led will be on 10second
    We also call __on__() and __off__() methods to turn on and off the leds
    '''

    redpin = 13
    greenpin = 12
    switchpin = 2

    while True:
        switchstate = pyduino_.__switch__(switchpin)
        if switchstate == 0:
            pyduino_.__off__(redpin)
            pyduino_.__on__(greenpin)
            print('on')
            
        else:
            pyduino_.__off__(greenpin)
            pyduino_.__on__(redpin)
            print('off')
            sleep(10)

    