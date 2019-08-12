"""
Import Source Chatbot Scripts
"""

import json
import src
import configparser

global environment
global appconfig

# Loads application environment
environment = configparser.ConfigParser()
environment.read('src/env/environment.cfg')

# Loads application configuration
appconfig = json.loads(open('uxy.json').read())





