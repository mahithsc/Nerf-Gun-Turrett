import serial.tools.list_ports

def get_port_name():
    ports = serial.tools.list_ports.comports()

    portList = []

    for onePort in ports:
        print(onePort)
        portList.append(onePort)


    portVar = input("From the selection above paste the first part of the serial port you wish to connect to: ")

    for i in portList:
        if portVar in i:
            print("You are now connected to serial port:", i)

def create_connection(portVar):
    serialInst = serial.Serial()

    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.close()
    serialInst.open()
    
    return serialInst


    

