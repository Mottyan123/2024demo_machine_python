from ultralytics import YOLO
import cv2

#学習したyoloの読み込み(train_xxのバージョン確認すること！！！)
model = YOLO("../runs/detect/train4/weights/last.pt")

results = model('./WIN_20240522_09_07_57_Pro.jpg')#画像認識を開始

from PIL import Image

for r in results:
    im_array = r.plot()
    im = Image.fromarray(im_array[..., ::-1])
    im.show()
    im.save('results_lobo2.jpg')

