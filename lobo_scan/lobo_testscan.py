from ultralytics import YOLO  
import cv2

#学習したyoloの読み込み
model = YOLO("../colab/02/last.pt")
cap = cv2.VideoCapture(0)#キャプチャーの読み込み

if not cap.isOpened():
    print("カメラを開けませんでした。")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("フレームを取得できませんでした。終了します。")
        break
    
    results = model(frame)
    
    im_annotated = results[0].plot()
    
    cv2.imshow('Camera', im_annotated)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows

