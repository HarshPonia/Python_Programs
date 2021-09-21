
# # OpenCV program to detect face in real time
# # import libraries of python OpenCV 
# # where its functionality resides
# import cv2 
  
# # load the required trained XML classifiers
# # https://github.com/Itseez/opencv/blob/master/
# # data/haarcascades/haarcascade_frontalface_default.xml
# # Trained XML classifiers describes some features of some
# # object we want to detect a cascade function is trained
# # from a lot of positive(faces) and negative(non-faces)
# # images.
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  
# # https://github.com/Itseez/opencv/blob/master
# # /data/haarcascades/haarcascade_eye.xml
# # Trained XML file for detecting eyes
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
  
# # capture frames from a camera
# cap = cv2.VideoCapture(0)
  
# # loop runs if capturing has been initialized.
# while 1: 
  
#     # reads frames from a camera
#     ret, img = cap.read() 
  
#     # convert to gray scale of each frames
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
#     # Detects faces of different sizes in the input image
#     faces = face_cascade.detectMultiScale(gray, 1, 5)
  
#     for (x,y,w,h) in faces:
#         # To draw a rectangle in a face 
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
  
#         # Detects eyes of different sizes in the input image
#         eyes = eye_cascade.detectMultiScale(roi_gray) 
  
#         #To draw a rectangle in eyes
#         for (ex,ey,ew,eh) in eyes:
#             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
  
#     # Display an image in a window
#     cv2.imshow('img',img)
  
#     # Wait for Esc key to stop
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
  
# # Close the window
# cap.release()
  
# # De-allocate any associated memory usage
# cv2.destroyAllWindows() 






















import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())

# load the video
camVideo = cv2.VideoCapture(args["video"])

# keep looping
while True:

    # grab the current frame and initialize the status text
    (grabbed, frame) = camVideo.read()
    status = "No Target in sight"

    # check to see if we have reached the end of the
    # video
    if not grabbed:
        break

    # convert the frame to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale
    blurred = cv2.GaussianBlur(gray, (7, 7), 0) #blur
    edged = cv2.Canny(blurred, 50, 150) #canny edge detection

    # find contours in the edge map
    (a, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
for cnt in a:
    approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),
    True)

    if len(approx)==5:
        cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
        status = "Target(s) in sight!"

        # draw the status text on the frame
        cv2.putText(frame, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX,
        0.5,(0, 0, 255), 2)

        # show the frame and record if a key is pressed
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    # if the 's' key is pressed, stop the loop
    if key == ord("s"):
        break

    # cleanup the input recorded video and close any open windows

camVideo.release()
cv2.destroyAllWindows()