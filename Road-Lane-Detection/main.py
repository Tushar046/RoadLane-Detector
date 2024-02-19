import cv2
import numpy as np
import image_processing
import lane_detection

cap = cv2.VideoCapture("Media/test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    canny_image=lane_detection.canny(frame)
    cropped_image=image_processing.region_of_interest(canny_image)

    lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
    averaged_lines=lane_detection.averaged_slope_intercept(frame,lines)
    line_image=lane_detection.display_line(frame,averaged_lines)
    combo_image=cv2.addWeighted(frame,0.8,line_image,1,1)
    
    cv2.imshow('Road LaneS',combo_image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()