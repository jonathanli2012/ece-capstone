import numpy as np
import cv2
from queue_struct import *
from sigs import *
from video_splice import *

MAX_FRAMES_IN_VIDEO = 2400

cap = cv2.VideoCapture('test_data.avi')  

q1 = queue_struct(512)
  
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = None
frames_recorded_out = 0

while(True):
    # reads frames from a camera 
    # ret checks return at each frame
    ret, frame = cap.read() 
  
    greyscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # The original input frame is shown in the window 
    cv2.imshow('Original', frame)
  
    # The window showing the greyscaled image
    cv2.imshow('frame', greyscaled_image)

    q1.enqueue_rear(greyscaled_image)
  
    # Wait for 'a' key to stop the program 
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

    # check for signal
    if CRASH_STATUS == "true":
        crash_saved_queue = q1.copy_queue
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        out.write(greyscaled_image)
        frames_recorded_out += 1
        CRASH_STATUS == "handled"

    elif CRASH_STATUS == "handled":
        if(frames_recorded_out == MAX_FRAMES_IN_VIDEO):
            CRASH_STATUS == "false"
            #finish processing video
            splice_queue_and_video(q1, out)
        else:
            out.write(greyscaled_image)
            frames_recorded_out += 1

cap.release()
out.release() 
cv2.destroyAllWindows()