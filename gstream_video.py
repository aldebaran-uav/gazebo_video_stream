import cv2 as cv

pipeline = 'udpsrc port=5600 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264" ! rtph264depay ! avdec_h264 ! videoconvert ! appsink sync=false'
cap = cv.VideoCapture(pipeline, cv.CAP_GSTREAMER)

while True:

    ret, frame = cap.read()


    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
 

cap.release()
