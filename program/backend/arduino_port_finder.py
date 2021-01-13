'''
finding Port name contain Arduino(Official Genuino Board) or CH340
'''

def arduino_port_finder(ports_dict):

        # Scanning avaliable port
    for port in ports_dict.keys():
        if 'Arduino' in ports_dict[port]: return port

        if 'CH340' in ports_dict[port]: return port

