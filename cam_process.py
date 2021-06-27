import cv2
import numpy as np
from collections import deque
import os
video="video/saida02.mp4"
cap=cv2.VideoCapture(video)
sub=cv2.createBackgroundSubtractorMOG2(detectShadows=False)
elemento_estruturante=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

points=deque(maxlen=20)
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        print("fim do video")
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.blur(gray,(7,7))

    fundo=sub.apply(gray)
    fundo = cv2.morphologyEx(fundo, cv2.MORPH_OPEN, elemento_estruturante, iterations=1)
    fundo=cv2.morphologyEx(fundo,cv2.MORPH_CLOSE,elemento_estruturante,iterations=3)
    print(np.sum(fundo))
    if np.sum(fundo)<300000:
        if len(points)>0:
            points.pop()
    else:
        contorno=cv2.findContours(fundo,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]
        contorno=sorted(contorno,key=cv2.contourArea,reverse=True)[:1]
        (cx,cy),raio=cv2.minEnclosingCircle(contorno[0])
        cv2.circle(frame,(int(cx),int(cy)),int(raio),(0,255,0),2)
        points.append([int(cx),int(cy)])

        if len(points)>18:
            if not os.path.isfile("imagem_evento/movimento.jpg"):
                cv2.imshow("evento",frame)
                cv2.imwrite("imagem_evento/movimento.jpg",frame)

        for (cx1,cy1) in points:
            cv2.circle(frame, (cx1, cy1), 5, (0, 0, 255), 2)


    cv2.imshow("frame",frame)
    tecla=cv2.waitKey(30)
    if tecla==ord("q"):
        break