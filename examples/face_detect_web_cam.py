from subprocess import Popen
import numpy as np
import cv2

# download haar cascades from: https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

# set dimensions of video
video_capture.set(3, 1280)
video_capture.set(4, 720)

# save videos as avi, 25.0 fps, at 1280x720
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 25.0, (1280,720))

scale = 0.2

while True:
    # read a frame from the camera
    ret, frame = video_capture.read()

    # write a frame out
    out.write(frame)

    height, width = frame.shape[:2]
    scaled = cv2.resize(frame, (int(scale*width), int(scale*height)))

    # convert to grayscale for face detection
    gray = cv2.cvtColor(scaled, cv2.COLOR_BGR2GRAY)

    # find faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    # draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (int(x/scale), int(y/scale)), (int((x + w)/scale), int((y + h)/scale)), (0, 255, 0), 2)

    # show the frame
    cv2.imshow('Video', frame)

    # quit the program if you hit "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
out.release()
cv2.destroyAllWindows()
