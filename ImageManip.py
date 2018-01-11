import PIL
import math

class ImageManip:
    def __init__(self, imageObj):
        self.image = imageObj

    def rotate(self, degrees):
        self.image.rotate(degrees).expand()






