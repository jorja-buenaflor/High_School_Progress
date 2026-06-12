import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame.")
        break
    neon_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('MacBook Webcam Feed', neon_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


