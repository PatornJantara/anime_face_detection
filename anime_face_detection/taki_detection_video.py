import cv2
t = 0
cap = cv2.VideoCapture('taki.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier('myhaar.xml')
    rects = detector.detectMultiScale(gray, minNeighbors=2 , minSize=(100,100))
    # draw rectangle cropping cat face
    if rects != ():
        for (i, (x, y, w, h)) in enumerate(rects):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, "Taki #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    
    cv2.imshow("Taki detector", frame)
    cv2.imwrite('taki{}'.format(t)+'.png',frame)
    t = t + 1

    k = cv2.waitKey(1)
    if  k%256 == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
