import pyfirmata

class Arduino:
    def __init__(self) -> None:
        self.board = pyfirmata.Arduino('/dev/ttyACM0')
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()

        # different pins on board
        self.led = self.board.get_pin('d:13:o')

    def turn_light_on(self):
        self.led.write(1)
    
    def turn_light_off(self):
        self.lef.write(0)