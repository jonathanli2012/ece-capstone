import numpy as np
import cv2
from queue_struct import *
  
cap = cv2.VideoCapture('tmp.avi')  

q1 = queue_struct(512)
  
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
  
while(True):
    # reads frames from a camera 
    # ret checks return at each frame
    ret, frame = cap.read() 
  
    greyscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      
    # output the frame
    out.write(greyscaled_image)
      
    # The original input frame is shown in the window 
    cv2.imshow('Original', frame)
  
    # The window showing the greyscaled image
    cv2.imshow('frame', greyscaled_image)

    q1.enqueue_rear(greyscaled_image)
  
      
    # Wait for 'a' key to stop the program 
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
  
cap.release()
out.release() 
cv2.destroyAllWindows()