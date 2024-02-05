import serial.tools.list_ports

def setup_serial(baud_rate=115200):

    ports = serial.tools.list_ports.comports()
    serial_inst = serial.Serial()

    port_list = []

    for port in ports:
        port_str = str(port)
        port_list.append(port_str)
        print(port_str)
        
        val = input("Select port: COM")
        
    for i in range(len(port_list)):
        
        if port_list[i].startswith("COM" + str(val)):
            port_var = "COM" + str(val)
            
    serial_inst.baudrate = baud_rate
    serial_inst.port = port_var
    
    return serial_inst
