import serial.tools.list_ports


def ms_windows_serial_scanner():
    ports_dict = {}
    for serial_port in [str(port) for port in list(serial.tools.list_ports.comports())]:
        port = serial_port.split('-')[0]
        device = serial_port[len(port) + 2:]
        if device.find(('(')) != -1: ports_dict[port] = device[:device.find('(') - 1]

    return ports_dict


