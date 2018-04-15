import cv2
import numpy as np


def trackbar_callback(x):
    pass


def zadanie0():
    """
    In this example I'm going to create a window with 3 trackbars, each for
    a different RGB (in OpenCV - BGR) value
    """
    # creating a color image 512x300 using numpy zeros() function
    img = np.zeros([300, 520, 3], dtype=np.uint8)
    cv2.namedWindow('window')
    
    # creating seperate trackbars for each color in BGR
    cv2.createTrackbar('B', 'window', 0, 255, trackbar_callback)
    cv2.createTrackbar('G', 'window', 0, 255, trackbar_callback)
    cv2.createTrackbar('R', 'window', 0, 255, trackbar_callback)

    while True:
        cv2.imshow('window', img)
        k = cv2.waitKey(1)

        if k == ord('q'):
            break

        # getting the values from each trackbar
        b = cv2.getTrackbarPos('B', 'window')
        g = cv2.getTrackbarPos('G', 'window')
        r = cv2.getTrackbarPos('R', 'window')
        
        # altering the image
        img[:] = [b, g, r]

    cv2.destroyAllWindows()


def zadanie1():
    """
    In this example I'm going to present binary thresholding. It's going to work
    this way: if pixel's value is lower than threshold its value is assigned to
    one value, elseways - another.
    ---------------------------
    We can achieve it using cv2.THRESH_... function. In case of binary thresholding
    - cv2.THRESH_BINARY()
    the first parameter is the source image, which should be a grayscale image
    the second parameter is the threshold value
    the third parameter is the maxVal which stands for the value to be assigned
    in case the pixel's value is greater then threshold
    """
    # types of thresholds
    threshold_types = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, \
                       cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV]
    img = cv2.imread('breugel.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('window')

    cv2.createTrackbar('binary_threshold', 'window', 0, 255, trackbar_callback)
    cv2.createTrackbar('threshold_type', 'window', 0, 4, trackbar_callback)

    while True:
        # getting the type of the threshold
        type = cv2.getTrackbarPos('threshold_type', 'window')
        # getting the value of threshold from the trackbar
        threshold = cv2.getTrackbarPos('binary_threshold', 'window')
        ret, thresh = cv2.threshold(img, threshold, 255, threshold_types[type])
        # altering the image
        cv2.imshow('window', thresh)
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            break
        
    cv2.destroyAllWindows()


def zadanie2():
    """
    In this example I'm going to resize an image using different interpolation methods.
    - INTER_NEAREST - interpolation which uses nearest neighbor
    - INTER_LINEAR - interpolation used by default - bilinear
    - INTER_AREA - interpolation which uses pixel area relation
    - INTER_CUBIC - bicubic interpolation over 4x4 pixel neighborhood
    - INTER_LANCZOS4 - Lanczos interpolation over 8x8 pixel neighborhood
    -----------------
    It all can be achieved using cv2.resize() method
    the first parameter is the image itself
    the second parameter is dsize which tells the program the desired size
    in case we want to specify the scaling, we can use fx and fy parameters;
    however, before we should set dsize as (0, 0) and then for example fx=1.5 and fy=1.5
    the last parameter specifies the interpolation method which should be used
    """
    img = cv2.imread('qr.jpg')
    
    tick = cv2.getTickCount()
    img_resized = cv2.resize(img, (0, 0), fx=1.75, fy=1.75)
    print('Time passed: ', (cv2.getTickCount() - tick)/1000, '[ms]')
    cv2.imshow('window', img_resized)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

    # exactly the same as above
    img = cv2.imread('qr.jpg')
    img_resized2 = cv2.resize(img, (0, 0), fx=1.75, fy=1.75, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('window', img_resized2)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

    img_resized3 = cv2.resize(img, (0, 0), fx=1.75, fy=1.75, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('window', img_resized3)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

    img_resized4 = cv2.resize(img, (0, 0), fx=1.75, fy=1.75, interpolation=cv2.INTER_AREA)
    cv2.imshow('window', img_resized4)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

    img_resized5 = cv2.resize(img, (0, 0), fx=1.75, fy=1.75, interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow('window', img_resized5)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()


def zadanie3():
    """
    All the images are being saved as the matrices, which we can use for different types
    of operations - element-wise operations (each element with a corresponding element from
    another matrix).
    --------------
    x = np.uint8([250])
    y = np.uint8([10])
    cv2.add() - adding two images together, 250 + 10 = 260 => 255, if not 250 + 10 = 260%256 = 4
    cv2.addWeighted(img1, alpha, img2, beta, gamma) - adding two images, however there's 
    a weight coresponding to each image (alpha, beta) and a bias (gamma); such weighted adding
    gives a feeling of blending or transparency.
    There are also bitwise operation which can be used on the images:
    cv2.bitwise_and()
    cv2.bitwise_or()
    cv2.bitwise_not()
    cv2.bitwise_xor()
    These come in handy while extracting any parts of the image which is not rectangular.
    ---------------
    In this example I'm going to blend two images and alter alpha and beta coefficcients'
    values using trackbars.
    """
    logo = cv2.imread('logo.png')
    painting = cv2.imread('breugelcrop.jpg')

    cv2.namedWindow('window')
    cv2.createTrackbar('alpha', 'window', 0, 1000, trackbar_callback)
    cv2.createTrackbar('beta', 'window', 0, 1000, trackbar_callback)

    while True:
        alpha_val = cv2.getTrackbarPos('alpha', 'window')/1000
        beta_val = cv2.getTrackbarPos('beta', 'window')/1000
        
        img = cv2.addWeighted(logo, alpha_val, painting, beta_val, 0)
        cv2.imshow('window', img)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # zadanie0()
    # zadanie1()
    zadanie2()
    # zadanie3()
