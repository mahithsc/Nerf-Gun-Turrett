import pyfirmata
import time

class Arduino:
    def __init__(self, port) -> None:
        self.board = pyfirmata.Arduino(port)
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()
        self.led = self.board.get_pin('d:13:o')

    def on(self):
        self.led.write(1)
    
    def off(self):
        self.led.write(0)