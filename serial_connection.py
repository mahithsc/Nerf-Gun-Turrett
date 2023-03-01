import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

serialInst = serial.Serial()

portList = []

for onePort in ports:
    print(onePort)
    portList.append(onePort)


portVar = input("From the selection above paste the first part of the serial port you wish to connect to: ")

for i in portList:
    if portVar in i:
        print("You are now connected to serial port:", i)


serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()


while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'))