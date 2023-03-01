import serial.tools.list_ports

def create_connection():


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
        serialInst.close()
        serialInst.open()
    
    return serialInst


# while True:
#     if serialInst.in_waiting:
#         packet = serialInst.readline()
#         print(packet.decode('utf'))
#     serialInst.write("FOUND".encode('utf-8'))