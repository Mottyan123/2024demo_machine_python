import cv2
import time
import math
import numpy as np
import os
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import serial

class Robot:
    def __init__(self):
        self.path = [(0, 0)]  # 初期位置

    def move(self, dx, dy):
        current_x, current_y = self.path[-1]
        new_x = current_x + dx
        new_y = current_y + dy
        self.path.append((new_x, new_y))

    def return_to_start(self):
        current_x, current_y = self.path[-1]
        start_x, start_y = self.path[0]
        dx = start_x - current_x
        dy = start_y - current_y
        return dx, dy

    def print_path(self):
        print("ロボットの移動経路:")
        for i, (x, y) in enumerate(self.path):
            print(f"ステップ {i}: ({x}, {y})")
    
    def yolo_capture(self):
        _, img = cap.read()
        results = model.predict(img)
        for r in results:
            annotator = Annotator(img)
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0]  
                c = box.cls
                conf = box.conf[0] 
                if int(c) == 0 and conf >= 0.6:  
                    label = f"{model.names[int(c)]} {conf:.2f}" 
                    annotator.box_label(b, label)
                    data = f"{model.names[int(c)]}:{math.floor((b[0]+b[2])/2)}:{math.floor((b[1]+b[3])/2)}\n"
                    ser.write(data.encode())
                    print(f"Object {model.names[int(c)]}: X={math.floor((b[0]+b[2])/2)}, Y={math.floor((b[1]+b[3])/2)}, Confidence={conf:.2f}")
            img = annotator.result()
        cv2.imshow('YOLO V8 Detection', img)

if __name__ == "__main__":
    
    while True:
        os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0" #初期設定
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        model = YOLO('../colab/02/yolov8n.pt')
        ser = serial.Serial("COM9", 115200, timeout=0.1)
        time.sleep(2)
        
        robot = Robot()
        stop_flag1 = False
        stop_flag2 = False
        stop_flag3 = False
        
        try:
            # 初期待機ループ
            print("Press the spacebar to start...")
            while not stop_flag1 and not stop_flag2:
                _, img = cap.read()
                cv2.imshow('Press Space to Start', img)
                key = cv2.waitKey(1) & 0xFF
                if key == ord(' '):  # スペースキー
                    stop_flag2 = True
                elif key == 27:  # ESCキー
                    stop_flag1 = True

            cv2.destroyAllWindows()
            
            # 初動処理
            while not stop_flag1 and not stop_flag3:
                cv2.imshow('Dummy Window', np.zeros((1, 1), dtype=np.uint8))
                key = cv2.waitKey(1) & 0xFF
                if key == ord(' '):  # スペースキー
                    stop_flag3 = True
                elif key == 27:  # ESCキー
                    stop_flag1 = True

                ser.write(f"LYRX:{-25}:{0}\n".encode())  # 前に進む
                start_time = time.time()
                while time.time() - start_time < 3:
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord(' '):
                        stop_flag3 = True
                        break
                    elif key == 27:
                        stop_flag1 = True
                        break

                ser.write(f"R2A:{25}\n".encode())  # 右旋回
                start_time = time.time()
                while time.time() - start_time < 1:
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord(' '):
                        stop_flag3 = True
                        break
                    elif key == 27:
                        stop_flag1 = True
                        break

            cv2.destroyAllWindows()
            
            # メイン処理
            while not stop_flag1:
                robot.yolo_capture()
                key = cv2.waitKey(1) & 0xFF
                if key == 27:  # ESCキー
                    stop_flag1 = True

        except Exception as e:
            print(f"エラーが発生しました: {e}")

        finally:
            cap.release()
            cv2.destroyAllWindows()
            ser.close()
        
        if stop_flag1:
            print("Restarting...")
            continue  # メインループの最初に戻る
        else:
            break  # 正常終了の場合はループを抜ける
        
