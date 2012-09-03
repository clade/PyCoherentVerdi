""" Package for reading parameters of the Verdi laser 

example:

verdi = VerdiDriver(port='COM7')
print verdi.power # print the measured power
print verdi.set_power # print the set power
verdi.set_power = 15.6 # set the power to 15.6 watts 
"""

import serial
from VerdiQuery import VerdiQueryClass, VerdiQueryList

DEFAULT_PORT='COM7'

class BaseDriver(serial.Serial):
    def __init__(self, port=DEFAULT_PORT, baudrate=19200, parity='N', stopbits=1 ):
        super(BaseDriver, self).__init__(port=port, baudrate=baudrate, parity=parity)
        
    def write_cmd(self, cmd, value):
        self.write('%s:%s\r\n'%(cmd, value))
        self.readline()
    def read_txt(self, cmd):
        """ Return the result of the command ?cmd """
        self.write('?%s\r\n'%cmd)
        a=self.readline().strip()
        if a=='': a=self.readline().strip()
        if 'Error' in a:
            raise Exception(a)
        if a[:6]=="VERDI>":
            a = a[6:]
        if '?%s'%cmd in a: a=a.replace('?%s'%cmd,'')
        return a
    
    def read_number(self, cmd):
        a = self.read_txt(cmd)
        return eval(a)

    def read_dict_number(self, cmd, dic):
        """ Return the result of the command ?cmd using a human readable output provided by dic """
        a = self.read_number(cmd)
        return dic[a]

    def read_list_cmd(self, liste_cmd):
        return dict([(cmd, self.__getattribute__(cmd)) for cmd in liste_cmd])

class VerdiCommand(object):
    @property
    def set_power(self):
        """Returns or set the light regulation set power in watts"""
        return super(VerdiCommand, self).set_power   
    @set_power.setter
    def set_power(self, value):
        self.write_cmd('P',"%6.4f"%value)

    @property
    def shutter(self):
        """Returns or set the status of the external shutter {0:"CLOSED", 1:"OPEN"}"""
        return super(VerdiCommand, self).shutter
    @shutter.setter
    def shutter(self, value):
        if value==True: value=1
        if value==False: value=0
        if isinstance(value, str):
            if value.lower()=='open': value=1
            if value.upper()=='close': value=0
        self.write_cmd('S',str(value))


        
class VerdiDriver(VerdiCommand, VerdiQueryClass,BaseDriver):
    """ Main class for driving the Verdi laser"""
    def read_all_parameters(self):
        return self.read_list_cmd(VerdiQueryList)

