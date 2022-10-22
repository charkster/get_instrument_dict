# get_instrument_dict
Python script that returns a dictionary of all **SCPI** instruments detected

Requirements:

**pip3 install pyvisa pyvisa-py pyusb**

Keys are the *IDN? query result and the values are the VISA resource name. Printing the dictionary is a quick way to display all connected instruments and list their associated resource name.

The following script will only list all resources. It is more useful to also include the instrument name.

**import pyvisa**

**rm = pyvisa.ResourceManager()**

**print(rm.list_resources())**


I use this dictionary for many different purposes in my bench automation.
