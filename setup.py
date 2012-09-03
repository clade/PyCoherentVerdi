# -*- coding: latin-1 -*-
import sys

#from distutils.core import setup
from setuptools import setup

long_description='''\
Overview
========

This package can be used to drive a Verdi laser using RS232


Installation
============

You need to connect the verdi laser to the computer using a RS232 port or a USB to RS232 converter
Identify the serial port on which the chiller is connecter ('COM..' on windows, '/dev/...' on linux)
You need to have the pyserial package installed

Usage
=====

from PyCoherentVerdi import VerdiDriver
verdi = VerdiDriver(port='COM7')
print verdi.power # print the measured power
print verdi.set_power # print the set power
verdi.set_power = 15.6 # set the power to 15.6 watts 

verdi.list_cmd(['power', 'baseplate_temperature']) # Returns a dictionary with the values of the parameters in the list
verdi.read_all_parameters() # Returns a dictionary with the values of all the parameters

Contact
=======

Please send bug reports or feedback to `Pierre Clade`_.

Version history
===============
Main changes:

* 0.2 Initial relase


.. _Pierre Clade: mailto:pierre.clade@spectro.jussieu.fr
'''


# There is a problem with writing unicode to a file on version of python <2.6
# So I remove the accent of the author name in this case
# TODO: find an automatic way of removing accent if version<2.6
if sys.version_info[:2]>=(2,6): # Unicode accent does not work on earlier version
    setup(name="PyCoherentVerdi", version='0.2',
      author=u'Pierre Cladé', author_email="pierre.clade@spectro.jussieu.fr",
      maintainer=u'Pierre Cladé',
      maintainer_email="pierre.clade@spectro.jussieu.fr",
      license='''\
This software can be used under one of the following two licenses: \
(1) The BSD license. \
(2) Any other license, as long as it is obtained from the original \
author.''',

      description='Interface to Tektronix Scope',
      long_description = long_description,  
      keywords=['Coherent','Verdi'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'], 
     requires=['pyserial'],
     packages=["PyCoherentVerdi", 'PyCoherentVerdi.example']

)
else: # version of python <2.6. Remove the unicode  
      setup(name="PyCoherentVerdi", version='0.2',
      author='Pierre Clade', author_email="pierre.clade@spectro.jussieu.fr",
      maintainer='Pierre Clade',
      maintainer_email="pierre.clade@spectro.jussieu.fr",
      license='''\
This software can be used under one of the following two licenses: \
(1) The BSD license. \
(2) Any other license, as long as it is obtained from the original \
author.''',

      description='Interface to the National Instrument PyDAQmx driver',

      long_description = long_description,

      keywords=['Coherent','Verdi'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'], 
     requires=['pyserial'],
     packages=["PyCoherentVerdi", 'PyCoherentVerdi.example']
)
