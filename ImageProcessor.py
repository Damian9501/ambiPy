from PIL import Image
import numpy as np

class ImageProcessor:
    def __init__(self, h, v):
        self.h = h
        self.v = v

    def processImage(self, input, output):
        img = Image.open(input)
        resultImage = img.resize((self.h, self.v), resample=Image.Resampling.BILINEAR)
        resultImage.save(output)

    def processImageArray(self, imageArray):
        img = Image.fromarray(imageArray)
        resultImage = img.resize((self.h, self.v), resample=Image.Resampling.BILINEAR)
        return resultImage

    def calculateColors(self, image):
        colorsList = []
        image_rgb = image.convert('RGB')
        # Quick reminder that we're counting leds from right-bottom corner of the screen and going anticlockwise
        for i in range(0, self.v, 1):
            colorsList.append((image_rgb.getpixel((self.h-1, i))))
        for i in range(self.h-1, -1, -1):
            colorsList.append((image_rgb.getpixel((i, self.v-1))))
        for i in range(self.v-1, -1, -1):
            colorsList.append((image_rgb.getpixel((0, i))))
        for i in range(0, self.h, 1):
            colorsList.append((image_rgb.getpixel((i, 0))))
        return colorsList

def imageProcessingTest():
    imageProcessor = ImageProcessor(13,7)
    imageProcessor.processImage('test_image.png', 'test_image_processed.png')

#imageProcessingTest()