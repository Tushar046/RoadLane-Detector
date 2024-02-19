import cv2
import numpy as np

def region_of_interest(image):
    height=image.shape[0]
    triangles=np.array([
        [(200,height),(1100,height),(550,250)]
    ])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,triangles,(255,255,255))
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image
