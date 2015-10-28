__author__ = 'ryanvade'

import base as b
import os
import sys
from serial import serialcli

class fromBase(b.base):
    def __init__(self):
        b.base.__init__(self) # should we need to call the supers constructor
        self.value = "Sub Class"
        self.whoAmI = "The Sub Class"
        self.cwd = os.getcwd()