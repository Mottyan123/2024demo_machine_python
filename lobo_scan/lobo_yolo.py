from ultralytics import YOLO

#学習したyoloの読み込み(train_xxのバージョンを確認すること！！！)
model = YOLO("../runs/detect/train6/weights/last.pt")

results = model.train(data='C:/Users/hkazu/OneDrive/ドキュメント/ロボプロ/学内ロボコン/python/lobo_scan/dust.yaml', epochs=500, patience=0, batch=32, device='cpu')


