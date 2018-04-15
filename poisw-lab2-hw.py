import cv2
import numpy as np


def negative():
    """
    In this example my goal is to create a negative img from the original one.
    We can achieve it using arithmetic operations on images, similarly to matrix operation.
    """
    img = cv2.imread('breugel.jpg', cv2.IMREAD_COLOR)
    cv2.namedWindow('window')
    
    negative_img = 255 - img    

    cv2.imshow('window', negative_img)
    k = cv2.waitKey(0)
    if k == ord('q'):
        cv2.destroyAllWindows()


if __name__ == '__main__':
    negative()

