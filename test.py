import main
from time import sleep



a = main.pyduino('/dev/cu.usbmodem142301')
bluePin = 13
switchPin = 2

if __name__ == '__main__':
    while True:
        switchstate = a.__switch__(switchPin)
        if switchstate == 1:
            a.__on__(bluePin)
            print('on')
            sleep(1)
            
        else:
            a.__off__(bluePin)
            print('off')
        
