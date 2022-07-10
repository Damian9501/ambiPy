import json
import Capture
import ColorRange
import LedStrip
from Functions import *

# Configuration
VERSION = '0.1.0.0'

run = True
config = json.load(open('config.json'))

# Main function
print('ambiPy v.' + VERSION + ' by Aleksander Heese \n' + breakText())

while(run):
    print('')