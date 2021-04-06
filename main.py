import cv2;

def picture_from_webcam():
    cam = cv2.VideoCapture(0);
    result = True;
    while (result):
        ret, frame = cam.read();
        print(ret);
        cv2.imwrite('CamPicture.jpg', frame);
        result = False;

    cam.release();
    cv2.destroyAllWindows();    

picture_from_webcam();         