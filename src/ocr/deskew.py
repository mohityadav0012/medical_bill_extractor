import cv2
import numpy as np

def deskew_image(img):
    coords=np.column_stack(np.where(img>0))
    angle=cv2.minAreaReact(coords)[-1]
    if angle<-45:
        angle=-(90+angle)

    else:
        angle=-angle
    (h,w)=img.shape[:2]
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,angle,1.0)
    rotated=cv2.warpAffine(img,M,(w,h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated