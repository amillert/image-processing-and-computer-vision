import cv2

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    key = ord('a')

    while key != ord('q'):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame comes here
        # Convert RGB image to grayscale
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Blur the image
        img_filtered = cv2.GaussianBlur(img_gray, (7, 7), 1.5)
        # Detect edges on the blurred image
        img_edges = cv2.Canny(img_filtered, 0, 30, 3)

        # Display the result of our processing
        cv2.imshow('result', img_edges)
        # Wait a little (30 ms) for a key press - this is required to
        # refresh the image in our window
        key = cv2.waitKey(30)

    # When everything done, release the capture and destroy created windows
    cap.release()
    cv2.destroyAllWindows()
