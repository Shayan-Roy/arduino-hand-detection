import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject

webcame=cv2.VideoCapture(0)
detector= HandDetector(detectionCon=0.8, maxHands=1)
arduino= SerialObject()
while True:
    success, img= webcame.read()
    hands, img = detector.findHands(img,flipType=False)

    if hands:
        lmlist=hands[0]
        fingerup=[]
        if lmlist:
            fingerup= detector.fingersUp(lmlist)
            print(fingerup)
        if fingerup==[0,1,0,0,0]:
            arduino.sendData([1])
            print("one led")
        elif fingerup==[0,1,1,0,0]:
             arduino.sendData([11])
             print("two led")
        elif fingerup==[1,0,0,0,0]:
            arduino.sendData([00])
    cv2.imshow("image",img)
    cv2.waitKey(1)