
from pyfirmata import Arduino, util
import time

class pyduino():

    def __init__(self, port):
        self.port = port
        

    def __on__(self, pin):
        '''
        This function turns on a led
        Argument: digital pin number
        '''
        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            pin = str(pin)
            self.pin = board.get_pin('d:'+pin+':o')

            self.pin.write(1)
        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')
        '''
        This function turns off a led
        Argument: digital pin number
        '''

    def __off__(self, pin):
        '''
        This function turns off a led
        Argument: digital pin number
        '''
        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            pin = str(pin)
            self.pin = board.get_pin('d:'+pin+':o')
            self.pin.write(0)
        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')
 
    
    def __switch__(self, pin):
        '''
        This function gives you the state of a switch (1 or 0)
        Argument: digital pin number
        '''
        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            pin = str(pin)
            self.pin = board.get_pin('d:'+pin+':i')
            return self.pin.read()
        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')



    def __pot__(self, pin):
        '''
        This function gives you the value of a potentiometer
        Argument: analog pin number
        '''

        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            pin = str(pin)
            self.pin = board.get_pin('a:'+pin+':i')
            return self.pin.read()
        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')

        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            pin = str(pin)
            self.pin = board.get_pin('a:'+pin+':i')
            return self.pin.read()

        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')

    def __tmp102__(self, pin, unity):
        '''
        This function gives you the value of a temperature sensor
        Argument: analog pin number
        unniity: c or f
        '''
        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            pin = str(pin)
            self.pin = board.get_pin('a:'+pin+':i')
            sensorVal = self.pin.read()
            voltage = sensorVal * 5.0
            if unity == 'C'.lower():
                temp = (voltage - 0.5) * 100
                return temp
            elif unity == 'F'.lower():
                temp = (voltage - 0.5) * 100 * 9/5 + 32
                return temp

        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')
        
    

    def __HC_SR01PIR__(self, pin):
        '''
        This function gives you the value of a HC-SR04 sensor
        Argument: digital pin number
        '''
        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            pin = str(pin)
            self.pin = board.get_pin('d:'+pin+':i')
            pirvalue = self.pin.read()
            if pirvalue is not None:
                return pirvalue
        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')
            
            
    def __analogJoystick__(sw_pin, Xpin, Ypin):
        '''
        This function gives you the position of a joystick
        Argument: 
        sw_pin: digital pin number
        Xpin: analog pin number
        Ypin: analog pin number
        '''
        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            sw_pin = str(sw_pin)
            Xpin = str(Xpin)
            Ypin = str(Ypin)
            sw_pin = board.get_pin('d:'+sw_pin+':i')
            Xpin = board.get_pin('a:'+Xpin+':i')
            Ypin = board.get_pin('a:'+Ypin+':i')
            if Xpin is not None and Ypin is not None:
                return (Xpin.read(), Ypin.read())

        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')