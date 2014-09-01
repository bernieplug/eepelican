from __future__ import with_statement
from fabric.api import *
import os, datetime, sys, inspect

		
def build():
    local('pelican -s pelicanconf.py')
    with lcd('output'):
        local('python -m SimpleHTTPServer')

