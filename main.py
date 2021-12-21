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

    
    def __off__(self, pin):
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
        try:
            board = Arduino(self.port)
            it = util.Iterator(board)
            it.start()
            pin = str(pin)
            self.pin = board.get_pin('a:'+pin+':i')
            return self.pin.read()
        except:
            print('Error please check your port and make sure the arduino is connected and  you upload first Arduuino standard Firmata on the board and then run the program')


            
            