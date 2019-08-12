"""
Import Source Chatbot Scripts
"""

import json
import src
import configparser

global environment
global appconfig

environment = configparser.ConfigParser()
environment.read('src/env/environment.cfg')

appconfig = json.loads(open('uxy.json').read())




