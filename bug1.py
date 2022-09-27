import sys
import numpy as np
from PIL import Image
import math
import sys
from collections import deque
from copy import copy
import math
import random

class Pixel:
     def __init__(self, x, y, color):
         self.x = x
         self.y = y
         self.color = color
"""
Load landscape and identify blue start and red finish points.
Later, add in random obstacle generation.
"""
class Landscape:
    def __init__(self, input_image) -> None:
        self.input_image = Image.open(input_image)
        self.pixel_map = self.input_image.load()

        #random start finish points. Adjust if spawned on obstacle.
        self.start, self.finish = Pixel(random.randint(0, 99),random.randint(0, 99),(255, 0 ,0)), Pixel(random.randint(0, 99),random.randint(0, 99),(0, 0 ,255))
        for point in [self.start, self.finish]:
            r, g, b, p = self.input_image.getpixel((point.x,point.y))
            while (r,g,b) == (0,0,0):
                self.save_path()
                point.x, point.y = random.randint(0, 99),random.randint(0, 99)
                r, g, b, p = self.input_image.getpixel((point.x, point.y))
            self.pixel_map[point.x,point.y] = point.color

        self.save_path()

    def save_path(self):
        self.input_image.save("out.png")


class Bug1:
    def __init__(self, landscape):
        print("New bug 1")
        self.landscape = landscape
        # self.landscape.pixel_map[landscape.start.x, landscape.start.y] = (0,255,0)
        # self.landscape.save_path()
    
    def start(self):
        while True:
            self.motion_to_goal()

    """
    Sense 8 pixels around bug to see what it's 'touching'.
    """
    def sense(self):
        pass

    """
    Move a single pixel and leave behind faded trail color.
    """
    def step(self):
        pass
    
    """
    Follow boundary around object then depart from leavepoint on boundary closest to goal.
    Keep list of (point, distance) to determine best leave point.
    """
    def boundary_following(self, hit_point):
        pass

    """
    Move a step towards target.
    """
    def motion_to_goal(self):
        pass

if __name__ == "__main__":
    landscape = Landscape(sys.argv[1])
    bug1 = Bug1(landscape)