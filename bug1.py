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

        # Random start finish points. Adjust if spawned on obstacle.
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
        self.pos = landscape.start
        self.end_arr = np.array((self.landscape.finish.x, self.landscape.finish.y))
        # self.landscape.pixel_map[landscape.start.x, landscape.start.y] = (0,255,0)

    
    def start(self):
        while True:
            next_step = self.motion_to_goal()
            r, g, b, p = self.landscape.input_image.getpixel((next_step[0],next_step[1]))
            
            # Terminal case
            if (np.array_equal(next_step, self.end_arr)):
                exit("PATH COMPLETED")
            
            # Obstacle
            if (r,g,b) == (0,0,0):
                self.boundary_following()

            self.landscape.pixel_map[next_step[0],next_step[1]] = (0,255,0)
            self.pos.x, self.pos.y = next_step[0],next_step[1]
        
            self.landscape.save_path()

    
    """
    Follow boundary around object then depart from leavepoint on boundary closest to goal.
    Keep list of (point, distance) to determine best leave point.
    """
    def boundary_following(self):
        hit_point = self.pos

    """
    Fetch the next step coords in the direction that brings you closest to target.
    """
    def motion_to_goal(self):
        pos_arr = np.array((self.pos.x, self.pos.y))

        best_arr = copy(pos_arr)
        best_dist = np.linalg.norm(self.end_arr - best_arr)
        # print(best_arr, best_dist)
        for neighbor in [[0,1], [1,0], [0,-1], [-1,0],[1,1], [-1,-1], [1,-1], [-1,1]]:
            neighbor_arr = np.array((self.pos.x + neighbor[0], self.pos.y + neighbor[1]))
            neighbor_dist = np.linalg.norm(self.end_arr - neighbor_arr)
            if (neighbor_dist < best_dist):
                best_arr = neighbor_arr
                best_dist = neighbor_dist

        # print(best_arr, best_dist)
        return(best_arr)
                

if __name__ == "__main__":
    landscape = Landscape(sys.argv[1])
    bug1 = Bug1(landscape)
    bug1.start()