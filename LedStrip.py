import time
from rpi_ws281x import PixelStrip, Color
import argparse

class LedStrip:
    def __init__(self, port):
        self.port = port

    def showLeds(self, listOfColors):
        index = 0
        