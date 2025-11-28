import cv2
import numpy as np

def preprocess(img_path,save_path=None):
    img=cv2.imread(img_path)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=cv2.fastNlMeansDenoising(gray,h=10)
    thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    if save_path:
        cv2.imwrite(save_path,thresh)
    return thresh