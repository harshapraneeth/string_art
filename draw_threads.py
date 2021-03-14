import math
import studio
import utils
import random
import numpy as np

size, fps = (1080, 1080), 60
radius = min(size)//2-1
n_pins, n_lines = 1080, 2160
input_name = 'rakul.jpg'
output_name = 'rakul.mp4'
alpha = 0.25

dt = 2*math.pi/n_pins
center = (size[0]//2, size[1]//2)

pins = [(int(center[0]+radius*math.cos(dt*i)), int(center[1]+radius*math.sin(dt*i))) for i in range(n_pins)]
image = studio.resize_image(studio.load_image(input_name, 0), size)

frame = np.full((size[0], size[1], 3), 255, dtype=np.uint8)
for p in pins: frame[p[0], p[1]] = (0, 0, 255)

def source():
    global image
    start = 0

    for lc in range(n_lines):
        min_error, end = 999, start

        for i in range(n_pins):
            if i==start: continue

            error, ec = 0, 0
            for p in utils.line(pins[start], pins[i], step=1):
                p = (int(p[0]), int(p[1]))
                if p[0]>=0 and p[0]<size[0] and p[1]>=0 and p[1]<size[1]:
                    error, ec = error+image[p[0], p[1]], ec+1
            error = error//ec

            if error<min_error: min_error, end = error, i
            
        for p in utils.line(pins[start], pins[end]):
            p = (int(p[0]), int(p[1]))

            if p[0]>=0 and p[0]<size[0] and p[1]>=0 and p[1]<size[1]:
                image[p[0], p[1]], frame[p[0], p[1]] = 255, utils.rgba2rgb(frame[p[0], p[1]],(0,0,0,alpha))
        
        print('rendering:',lc,'of',n_lines, 'from', (start, end)); yield frame
        start = end

studio.create_video(output_name, fps, size, source())
studio.create_image('output.jpg',image)