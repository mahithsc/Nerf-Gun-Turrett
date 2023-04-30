from serial_connection import get_port_name
import pyfirmata


class ArduinoTest:
    def __init__(self, port) -> None:
        self.board = pyfirmata.Arduino(port)
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()

        # different pins
        self.led = self.board.get_pin('d:13:o')
        
        self.servo = self.board.get_pin('d:9:s')
        self.servo.write(0)

        self.servo2 = self.board.get_pin('d:10:s')
        self.servo2.write(0)

    def on(self):
        self.led.write(1)
    
    def off(self):
        self.led.write(0)
    
    def shoot(self):
        self.servo.write(130)
    
    def stop_shooting(self):
        self.servo.write(0)
    

if __name__ == '__main__':

    board = ArduinoTest(get_port_name())


 