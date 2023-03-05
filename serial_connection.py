import serial.tools.list_ports

def get_port_name():
    ports = serial.tools.list_ports.comports()

    port_list = []

    for one_port in ports:
        print(one_port)
        port_list.append(one_port)


    port_var = input("From the selection above paste the first part of the serial port you wish to connect to: ")

    for i in port_list:
        if port_var in i:
            print("You are now connected to serial port:", i)
            return port_var


def create_connection(portVar):
    serialInst = serial.Serial()

    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.close()
    serialInst.open()
    
    return serialInst


    

