import cv2
# import numpy as np


def slider():
    """
    The purpose of this exercise is to create a slider of few pictures.
    press n to view next picture
    press p to view previous picture
    press q to quit the slider
    After reaching the last picture in the set, slider should move
    to the beginning of the set, and vice versa... If one is trying to see
    the image before the 1st one, the last image should be displayed
    """

    _slider = []
    for i in range(3):
        title = 'bruegel' + str(i + 1) + '.jpg'
        print(title)
        _slider.append(cv2.imread(title, cv2.IMREAD_COLOR))

    print(len(_slider), type(_slider[2]))

    # testing, whether all images display correctly
    cv2.imshow('cos', _slider[0])
    key = cv2.waitKey()
    if key == ord('q'):
        cv2.destroyAllWindows()
    cv2.imshow('cos', _slider[1])
    key = cv2.waitKey()
    if key == ord('q'):
        cv2.destroyAllWindows()
    cv2.imshow('cos', _slider[2])
    key = cv2.waitKey()
    if key == ord('q'):
        cv2.destroyAllWindows()

    im = 0

    while True:
        cv2.destroyAllWindows()
        cv2.imshow('painting', _slider[im])
        # key = cv2.waitKey(0) & 0xFF
        if cv2.waitKey(0) & 0xFF == ord('n'):
            if im + 1 > len(_slider) - 1:
                im = 0
                cv2.destroyAllWindows()
            else:
                im += 1
                cv2.destroyAllWindows()
        elif cv2.waitKey(0) & 0xFF == ord('p'):
            if im - 1 < 0:
                im = len(_slider) - 1
                cv2.destroyAllWindows()
            else:
                im -= 1
                cv2.destroyAllWindows()
        elif cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print('quit')
            break

if __name__ == '__main__':
    slider()
