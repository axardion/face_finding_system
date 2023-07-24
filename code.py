import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img =  cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('faces.xml')

    results = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=1)

    for (x, y, width, height) in results:
            cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), thickness=1)
            cv2.putText(img, 'Face', (x, y -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

    cv2.imshow('result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break