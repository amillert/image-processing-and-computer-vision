import cv2


def zadanie1():
    """
    cv.imread - loading the image

    first parameter is the path to image,
    second - a flag specifying colors of image to be loaded
    --------------------------------------
    cv.write - saving the image

    first parameter specifies the path, where img will be saved,
    second specifies, which img to save
    --------------------------------------
    cv.imshow used for displaying the image

    first parameter specifies the name of the window, where img is being displayed,
    second - specifies the image to be displayed
    --------------------------------------
    cv2.waitKey - checking whether a certain key has been pressed for given period of time
    --------------------------------------
    cv2.destroyAllWindows - closing open windows
    --------------------------------------
    """

    img_color = cv2.imread('breugel.jpg', cv2.IMREAD_COLOR)
    img_grey = cv2.imread('breugel.jpg', cv2.IMREAD_GRAYSCALE)

    cv2.imshow('art', img_color)
    key = cv2.waitKey(0)
    # wait for ESC -- 27
    if key == 27:
        cv2.destroyAllWindows()
    elif key == ord('s'):
        cv2.imwrite('savedpic.jpg', img_color)
        cv2.destroyAllWindows()

    cv2.imshow('art', img_grey)
    key = cv2.waitKey(0)
    if key == 27:  # wait for ESC
        cv2.destroyAllWindows()

    return img_color, img_grey


def zadanie2(img_color, img_grey):
    """
    colors in openCV are not saved as RGB, instead - BRG
    referring to colors of some pixel works similarly to refering to element in the matrix
    BGR image consists of 3 channels,
    whereas black-and-white img - 1;
    similarly one can change colors of a pixel by altering values inside the image's matrix
    --------------------------------------
    cv2.split - splitting image into separate sub-images for each color-channel

    parameter passed specifies the image to be split
    --------------------------------------
    cv2.merge - works analogically, it merges sub-images for each color into one
    --------------------------------------
    cv2.resize - self-explanatory, resizing the image

    first parameter specifies the image to be resized,
    second used to rescale image in X-axis (e.g. fx-0.5 to make the image 2-times smaller in X-axis)
    third used to rescale image in Y-axis (e.g. fy-0.5 to make the image 2-times smaller in Y-axis)
    --------------------------------------
    """

    img_resize = cv2.resize(img_color, (0, 0), fx=0.7, fy=0.7)

    px_img_color = img_color[220, 270]
    px_img_grey = img_grey[220, 270]

    print('color image:', px_img_color)
    print('grey image:', px_img_grey)

    for x in range(200):
        for y in range(200):
            img_color[x, y] = [0, 0, 0]

    cv2.imshow('zaczernione', img_color)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

    print('img shape:', img_color.shape)

    b, g, r = cv2.split(img_color)
    cv2.imshow('blue', b)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
    cv2.imshow('green', g)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
    cv2.imshow('red', r)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

    sample_human = img_resize[500:600, 0:80]
    img_resize[0:100, 0:80] = sample_human
    cv2.imshow('doklejony', img_resize)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()


def zadanie3():
    kolka = cv2.imread('kolka.svg.webp', cv2.IMREAD_COLOR)
    cv2.imshow('kolka', kolka)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

    # b, g, r = cv2.split(kolka)
    # cv2.imshow('niebieskie', b)
    # key = cv2.waitKey(0)
    # if key == 27:
    #     cv2.destroyAllWindows()
    # cv2.imshow('zielone', g)
    # key = cv2.waitKey(0)
    # if key == 27:
    #     cv2.destroyAllWindows()
    # cv2.imshow('czerwone', r)
    # key = cv2.waitKey(0)
    # if key == 27:
    #     cv2.destroyAllWindows()


def zadanie4():
    """
    camera cv2.VideoCapture(0) - picking a default camera
    --------------------------------------
    frame = camera.read() - capturing a frame from a video
    --------------------------------------
    cv2.cvtColor - changing the color of a frame
    --------------------------------------
    camera.release() - turning off previously picked camera
    --------------------------------------
    """
    camera = cv2.VideoCapture(0)

    frame_no = 0
    file_name = 'cam_snap_'

    while(True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(file_name+str(frame_no)+'.jpg', gray)
            frame_no += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


def zadanie5():
    video = cv2.VideoCapture('Wildlife.mp4')

    while(True):
        ret, frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # key = cv2.waitKey(100)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def zadanie6():
    """
    openCV has built-in functions allowing one to draw shapes
    on an image, similarly one can put a text on the image
    --------------------------------------
    """
    img = cv2.imread('breugel.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0, 0), fx=0.6, fy=0.6)
    img = cv2.rectangle(img, (480, 0), (580, 750), (255, 255, 255), -1)
    cv2.imshow('img', img)

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img, 'Umim obrazy!', (10, 500), font, 3, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.imshow('img', img)

    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    img_color, img_grey = zadanie1()
    zadanie2(img_color, img_grey)
    zadanie3()
    zadanie4()
    # zadanie5()
    zadanie6()
