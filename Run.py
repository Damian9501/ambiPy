import json
from Capture import Capture
from ImageProcessor import ImageProcessor
from LedStrip import LedStrip
from Functions import *

# Configuration
VERSION = '0.1.0.0'

run = True
config = json.load(open('config.json'))

# Header
print('ambiPy v.' + VERSION + ' by Aleksander Heese \n' + breakText())

cap = Capture()
imgProc = ImageProcessor(config['layout']['horizontal'],config['layout']['vertical'])
ledStrip = LedStrip(config['preconfig']['ledPort'])

print(imgProc.calculateColors(imgProc.processImageArray(cap.captureImageArray())))

#while(run):
    #print('')