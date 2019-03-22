"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""

# Imported libraries into project

import serial
import serial.tools.list_ports
import time
import logging

EOL = "\n"

ser = serial.Serial()

class SerialCom:
    def __init__(self):
        pass

    def open(self, port, baud, timeout):
        ser.port = port
        ser.baudrate = baud
        ser.timeout = timeout
        if not ser.isOpen():
            ser.open()
        ser.flush()

    def close(self):
        ser.close()

    def sendCommand(self, command):
        ser.write(str(command) + EOL)

    def readData(self, End):
        return str(ser.read_until(terminator=End))

    def availablePorts(self):
        ports = list(serial.tools.list_ports.comports())
        return ports

    def isOpen(self):
        return ser.isOpen()