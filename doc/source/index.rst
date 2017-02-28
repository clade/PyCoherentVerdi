.. PyCoherentVerdi documentation master file, created by
   sphinx-quickstart on Wed Jan 23 10:44:55 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyCoherentVerdi's documentation!
===========================================


Package for reading parameters of the Verdi laser 

Note that the module uses property attributes. Look at the python documentation 
to understand how property attributes are working if you don't alread know. 

Example ::

    verdi = VerdiDriver(port='COM7')
    print verdi.power # print the measured power
    print verdi.set_power # print the set power
    verdi.set_power = 15.6 # set the power to 15.6 watts 

    verdi.list_cmd(['power', 'baseplate_temperature']) # Returns a dictionary with the values of the parameters in the list
    verdi.read_all_parameters() # Returns a dictionary with the values of all the parameters

Verdi API
=========

Main commands
-------------

.. automodule:: PyCoherentVerdi
.. autoclass:: VerdiDriver
   :members: read_all_parameters, read_list_cmd, set_power,
    shutter,
    laser,
    enable,
    stand_by

Verdi parameters
----------------

List of all the parameters that can be individually read.

.. automodule:: PyCoherentVerdi.VerdiQuery
.. autoclass:: VerdiQueryClass
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

