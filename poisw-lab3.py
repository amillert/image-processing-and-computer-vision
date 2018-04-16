import cv2
import numpy as np
import matplotlib.pyplot as plt
 
def nothing(x):
    pass
 
 
def zadanie1():
    img_salt = cv2.imread('lena_salt_and_pepper.bmp', cv2.IMREAD_GRAYSCALE)
    img_noise = cv2.imread('lena_noise.bmp', cv2.IMREAD_GRAYSCALE)
 
    cv2.namedWindow('window1')
    cv2.namedWindow('window2')
    cv2.namedWindow('window3')
 
    cv2.createTrackbar('size1', 'window1', 0, 20, nothing)
    cv2.createTrackbar('size2', 'window2', 0, 20, nothing)
    cv2.createTrackbar('size3', 'window3', 0, 20, nothing)
 
    while True:
        size1 = cv2.getTrackbarPos('size1', 'window1')
        size2 = cv2.getTrackbarPos('size2', 'window2')
        size3 = cv2.getTrackbarPos('size3', 'window3')
 
        blur = cv2.blur(img_salt, (2*size1+1, 2*size1+1))
        gaussianblur = cv2.GaussianBlur(img_salt, (2*size2+1, 2*size2+1),0)
        medianblur = cv2.medianBlur(img_salt, 2*size3+1)
 
        cv2.imshow('window1', blur)
        cv2.imshow('window2', gaussianblur)
        cv2.imshow('window3', medianblur)
 
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
 
    cv2.destroyAllWindows()
 
    cv2.namedWindow('window4')
    cv2.namedWindow('window5')
    cv2.namedWindow('window6')
 
    cv2.createTrackbar('size4', 'window4', 0, 20, nothing)
    cv2.createTrackbar('size5', 'window5', 0, 20, nothing)
    cv2.createTrackbar('size6', 'window6', 0, 20, nothing)
 
    while True:
        size4 = cv2.getTrackbarPos('size4', 'window4')
        size5 = cv2.getTrackbarPos('size5', 'window5')
        size6 = cv2.getTrackbarPos('size6', 'window6')
 
        blur = cv2.blur(img_noise, (2*size4+1, 2*size4+1))
        gaussianblur = cv2.GaussianBlur(img_noise, (2*size5+1, 2*size5+1),0)
        medianblur = cv2.medianBlur(img_noise, 2*size6+1)
 
        cv2.imshow('window4', blur)
        cv2.imshow('window5', gaussianblur)
        cv2.imshow('window6', medianblur)
 
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
 
    cv2.destroyAllWindows()
 
 
def zadanie2():
    img_gray = cv2.imread('breugel.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('window')
 
    cv2.createTrackbar('binary_threshold', 'window', 0, 255, nothing)
    cv2.createTrackbar('kernel', 'window', 0, 10, nothing)
 
 
    while True:
        # getting the value of threshold from the trackbar
        threshold = cv2.getTrackbarPos('binary_threshold', 'window')
        ret, thresh = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
 
        kernel_val = cv2.getTrackbarPos('kernel', 'window')
        kernel = np.ones((kernel_val, kernel_val), np.uint8)
        erosion = cv2.erode(thresh, kernel, iterations=1)
 
        # altering the image
        cv2.imshow('window', erosion)
        key = cv2.waitKey(1)
 
        if key == ord('q'):
            break
 
    cv2.destroyAllWindows()
 
 
def zadanie3():
    img_gray = cv2.imread('breugel.jpg', cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread('breugel.jpg', cv2.IMREAD_COLOR)
 
    # gray scale
    hist, bins = np.histogram(img_gray.ravel(), 256, [0, 256])
    plt.hist(img_gray.ravel(), 256, [0,256], color='k')
    plt.title('Histogram of an image')
    plt.xlabel('balck(left)         ----         white(right)')
    plt.ylabel('Amount of pixels')
    plt.show()
 
    #in color
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histogram = cv2.calcHist([img_color], [i], None, [256], [0, 256])
        plt.plot(histogram, color=col)
    plt.show()
 
 
def zadanie4():
    img_gray = cv2.imread('breugel.jpg', cv2.IMREAD_GRAYSCALE)
 
    cv2.imshow('window', img_gray)
    key = cv2.waitKey(0)
 
    if key == ord('q'):
        cv2.destroyAllWindows()
 
    equ = cv2.equalizeHist(img_gray)
    res = np.hstack((img_gray, equ))  # stacking images side-by-side
    cv2.imwrite('res.png', res)
    ress = cv2.imread('res.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('wind', ress)
 
    # cv2.imshow('window', img_gray)
    cv2.waitKey(0)
 
     # if key == ord('q'):
     #     cv2.destroyAllWindows()
 
 
 
if __name__ == '__main__':
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
