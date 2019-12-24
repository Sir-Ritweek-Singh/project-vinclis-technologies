import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)
#cap.open('http://192.168.137.107.4747/video')

i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ncut =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([94, 100, 43])
    upper_blue = np.array([126, 255, 255])
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    img = cv2.rectangle(gray, (0,0), (400, 2800), (0, 0, 0), -1)
    if ret == False:
        break
    cv2.imshow('output', ncut)
    cv2.imshow('output', frame)
    #cv2.imshow('blue', mask)
    nol = datetime.datetime.now()
    today = nol.strftime("%m.%d.%Y-%H.%M.%S")

    if cv2.waitKey(2) & 0xFF == ord('q'):
     if i==0:
         cv2.imwrite(today+'testgrey'+str(i)+'.jpg', img)
         print("Front image taken")
     else:
        cv2.imwrite(today +'testgrey' + str(i) + '.jpg', ncut)
        print(str(i+1)+"image has been taken")
        path = r'C:\Users\ritwe\OneDrive\Desktop'
        cv2.imwrite(r'C:\Users\ritwe\OneDrive\Desktop\testgrey'+today + str(i) + '.jpg', gray)
     cv2.imwrite(today+'testcolour'+str(i)+'.jpg', frame)
     print("colour")
     i+=1
    if cv2.waitKey(2) & 0xFF == ord('n'):
        i=0
        print("New patient")
    if cv2.waitKey(2) & 0xFF == ord('s'):
        break




# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()