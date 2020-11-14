Overview
========

This package can be used to drive a Verdi laser using RS232


Installation
============

- You need to connect the verdi laser to the computer using a RS232 port or a USB to RS232 converter.  
- Identify the serial port on which the laser is connected ('COM..' on windows, '/dev/...' on linux).
- You need to have the pyserial package installed.

- It is also possible to use any other interface that provide a read and write methods (for example brainboxes)

Usage
=====

::

    from PyCoherentVerdi import VerdiDriver
    verdi = VerdiDriver(port='COM7')
    print verdi.power # print the measured power
    print verdi.set_power # print the set power
    verdi.set_power = 15.6 # set the power to 15.6 watts

    verdi.read_list_cmd(['power', 'baseplate_temperature']) # Returns a dictionary with the values of the parameters in the list
    verdi.read_all_parameters() # Returns a dictionary with the values of all the parameters


Version history
===============
Main changes:

* 0.2 Initial relase
* 0.3 Add support for other interface


