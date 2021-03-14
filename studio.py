import cv2
import time
import numpy as np

def create_video(file_name, fps, size, source):
    start = time.time()
    out = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for frame in source: out.write(frame)
    out.release()
    print('----------- finished in',round(time.time()-start,3),'s -----------')

load_image = lambda file_name, mode: cv2.imread(file_name, mode)
resize_image = lambda image, size: cv2.resize(image, size)
create_image = lambda file_name, source: cv2.imwrite(file_name, source)