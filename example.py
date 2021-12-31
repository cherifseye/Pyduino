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

    #Example 3: Control two LED using a switch button

    '''
    We will make a control panel with a switch and lights turn on when you press the switch
    The green led will be on until the switch is pressed the red led will be on 10second
    We also call __on__() and __off__() methods to turn on and off the leds
    '''
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
    '''

    #Example 4: Control LED brightness using a potentiometer
    '''
     In this example we will control the brightness of the LED using a potentiometer
     The potentiometer will be connected to analog pin A0 and the LED will be connected to digital pin 13
     we will use a resistance to connect the potentiometer to the LED and allows us to set the resistance min to 222ohm then our led will not break
     We also provide a another complete example using GUI pyqt5 named SETUX wich is very helpful for beginner who want to contol their Arduino and their
     own board control.
     You can find this example in my git github repository named SETUX
     '''

    '''
     redpin = 13
     potpin = '0'
     while True:
         potvalue = pyduino_.__pot__(potpin)
         pyduino_.__on__(redpin)
         if potvalue is not None:
             print(potvalue)
     '''

    print('----------------------------------------------------------------------------------')

    #Example 5: The temperature monitor using a tmp102 sensor

    '''
    In this example we will use a tmp102 sensor to monitor the temperature we'll also use 2 leds (green and red)
    The tmp102 sensor is connected to analog pin A0 and the leds are connected to digital pins 9 and 10
    as a output in the terminal you can get the temperature value in celsius or fahrenheit (unity == 'c' or 'f')
    '''

    '''
    redpin = 9
    greenpin = 10
    tempPin = 0
    tempref = 20
    unity = 'c'
    while True:
        tempValue = pyduino_.__temp__(tempPin, unity)
        if tempValue is not None:
            if tempValue > tempref:
                pyduino_.__on__(redpin)
                pyduino_.__off__(greenpin)
                print('red')
            else:
                pyduino_.__on__(greenpin)
                pyduino_.__off__(redpin)
                print('green')
    '''
    
    #Example 6: Move detection using pir sensor
    '''
    In this example we will use a pir sensor to detect if someone is moving in the room we'll also use a green led
    The pir sensor is connected to digital pin 7 and the led is connected to digital pin 13
    If the pir sensor detects a movement the led will turn on
    '''

    '''
    board = Arduino(self.port)
    it = util.Iterator(board)
    it.start()
    ledpin = board.get_pin('d:13:o')
    pirpin = 7
    pirValue = pyduino_.__HC_SR04__(pirpin)
    while True:
        ledpin.write(pirValue)
         
    '''
        

