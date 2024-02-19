import cv2
import numpy as np

def canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def display_line(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)  # Corrected line color
    return line_image

def make_coordinates(image, line_parameters):
    slope,intercept=line_parameters
    
    y1=image.shape[0]
    y2=int(y1*(3/5))
    x1=int((y1-intercept)/slope)
    x2=int((y2-intercept)/slope)

    return np.array([x1,y1,x2,y2])
     
def averaged_slope_intercept(image,lines):
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters=np.polyfit((x1,x2),(y1,y2),1)
        slope=parameters[0]
        intercept=parameters[1]

        if slope<0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))

    average_left_fit=np.average(left_fit,axis=0)
    average_right_fit=np.average(right_fit,axis=0)

    left_line= make_coordinates(image,average_left_fit)
    right_line=make_coordinates(image,average_right_fit)

    return np.array([left_line,right_line]) 
