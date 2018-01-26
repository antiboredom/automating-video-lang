import time
import numpy as np
import cv2
import ipcamera

video_capture = cv2.VideoCapture(ipcamera.MJPG_URL)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

last_moved = time.time()
recording = 0

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, minSize=(60, 60))

    for face in faces:
        x = face[0]
        y = face[1]
        w = face[2]
        h = face[3]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    
    current_time = time.time()
    if len(faces) > 0 and current_time - last_moved > 3:
        face = sorted(faces, key=lambda f:f[2])[-1]
        ipcamera.center(face[0], face[1])
        ipcamera.record('face-' + str(recording) +'.mp4', '00:00:03', rtsp=True)
        ipcamera.relative_zoom(1000)
        time.sleep(3)
        ipcamera.relative_zoom(-1000)
        last_moved = time.time()
        recording += 1


    # cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
