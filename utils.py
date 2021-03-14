import random
import math
import numpy as np

random_point = lambda n, _min, _max: tuple(random.randint(_min[i], _max[i]) for i in range(n))
center = lambda p1, p2: tuple(( (p1[0]+p2[0])/2, (p1[1]+p2[1])/2 ))
distance = lambda n, p1, p2: math.sqrt( sum( ((p1[i]-p2[i])**2 for i in range(n)) ) )
min_max = lambda a, b: (a, b) if a<b else (b, a)
slope = lambda p1, p2: math.inf if round(p1[0]-p2[0], 4)==0 else (p1[1]-p2[1]) / (p1[0]-p2[0])
inside_circle = lambda x,y,c,r: (x-c[0])**2+(y-c[1])**2<r**2

def rgba2rgb(c1, c2):
    a = c2[3]
    return ( 
        (1-a)*c1[0] + a*c2[0],
        (1-a)*c1[1] + a*c2[1],
        (1-a)*c1[2] + a*c2[2]
     )

def line(p1, p2, step=1):
    if round(p1[0]-p2[0], 4)==0:
        y_min, y_max = min_max(p1[1], p2[1])
        while y_min<=y_max: yield (p1[0], y_min); y_min += step
    else:
        m = round( (p1[1]-p2[1])/(p1[0]-p2[0]), 4 )
        c = round( p1[1]-m*p1[0], 4 )
        x_min, x_max = min_max(p1[0], p2[0])
        x_prev, y_prev = x_min, m*x_min+c
        while x_prev<x_max:
            x_new, y_new = x_prev+step, m*(x_prev+step)+c
            y1, y2 = min_max(y_prev, y_new)
            while y1<y2: yield (x_prev, y1); y1 += step
            yield (x_new, y_new)
            x_prev, y_prev = x_new, y_new

def rotate(p, c, a):
    p = (p[0]-c[0], p[1]-c[1])
    cos_a, sin_a = math.cos(a), math.sin(a)
    return (round(p[0]*cos_a-p[1]*sin_a+c[0], 4), round(p[0]*sin_a+p[1]*cos_a+c[1], 4))

class shape:
    def __init__(self, n_sides, center, radius, thickness=1, corners=[]):
        self.n, self.c, self.r, self.t, self.cr = n_sides, center, radius, thickness, corners
    
    def get_corners(self, r):
        a = math.pi*2/self.n
        return [(round(self.c[0]+r*math.sin(i*a-math.pi/2), 4), round(self.c[1]+r*math.cos(i*a-math.pi/2), 4)) for i in range(self.n)]

    def get(self):
        for i in range(-self.t//2, self.t//2+1):
            self.cr = self.get_corners(self.r+i)
            for j in range(self.n):
                for p in line(self.cr[j], self.cr[(j+1)%self.n]): yield p









