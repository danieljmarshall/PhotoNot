import PIL
import math

class ImageManip:
    def __init__(self, imageObj):
        self.image = imageObj

    def rotate(self, degrees):
        self.image.rotate(degrees).expand()

    def rotate90(self):
        self.image.rotate(90).expand()

    def resize(self, size):
        self.image.resize(size)

    def resize_50(self):
        new_size = self.image.size * 0.5
        self.image.resize(new_size)

    def resize_150(self):
        new_size = self.image.size * 1.5
        self.image.resize(new_size)

    def resize_200(self):
        new_size = self.image.size * 2
        self.image.resize(new_size)





