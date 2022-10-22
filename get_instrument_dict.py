def get_instrument_dict():
    # this dictionary is the IDN string as the key and the instrument address as the value
    instrument_dict = {}
    rm = pyvisa.ResourceManager()
    # rm = pyvisa.ResourceManager('@py')
    for inst in rm.list_resources():
        try:
            if (str(inst).startswith('ASRL')): # set the max baud rate for all usb serial ports
                handle = rm.open_resource(inst, baud_rate=19200)
            else:
                handle = rm.open_resource(inst)
        except:
            print("failed " + str(inst))
        else:
            try:
                instrument_idn = handle.query('*IDN?')
            except:
                pass
            else:
                instrument_dict[instrument_idn] = inst
    return instrument_dict
