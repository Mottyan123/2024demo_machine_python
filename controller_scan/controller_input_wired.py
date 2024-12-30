import pygame
import serial 
import time
import math

# シリアルポートの設定
ser = serial.Serial("COM4", 115200, timeout=0.1)
time.sleep(2)

# Pygameの初期化
pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
print("pygame初期化完了")

print("コントローラーを操作してください")
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.JOYBUTTONDOWN:  # ボタンが押された場合
            if event.button == 0:
                print("□ボタンが押されました")
                ser.write(f"SB:{1}\n".encode())
                time.sleep(0.05)
            if event.button == 1:
                print("バツボタンが押されました")
                ser.write(f"XB:{1}\n".encode())
                time.sleep(0.05)
            if event.button == 2:
                print("マルボタンが押されました")
                ser.write(f"CB:{1}\n".encode())
                time.sleep(0.05)
            if event.button == 3:
                print("△ボタンが押されました")
                ser.write(f"TB:{1}\n".encode())
                time.sleep(0.05)
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                print("□ボタンが離されました")
                ser.write(f"SB:{0}\n".encode())
                time.sleep(0.05)
            if  event.button == 1:
                print("バツボタンが離されました")
                ser.write(f"XB:{0}\n".encode())
                time.sleep(0.05)
            if  event.button == 2:
                print("マルボタンが離されました")
                ser.write(f"CB:{0}\n".encode())
                time.sleep(0.05)
            if event.button == 3:
                print("△ボタンが離されました")
                ser.write(f"TB:{0}\n".encode())
                time.sleep(0.05)
        elif event.type == pygame.JOYAXISMOTION:
            if abs(j.get_axis(5)) >0:
                rs_y = math.floor(j.get_axis(5) * 255)
                ser.write(f"RSY:{rs_y}\n".encode())
                print(f"RSY: {rs_y}")
            if abs(j.get_axis(1)) >0 or abs(j.get_axis(2)) >0:
                ls_y = math.floor(j.get_axis(1) * 25)
                rs_x = math.floor(j.get_axis(2) * 25)
                ser.write(f"LYRX:{ls_y}:{rs_x}\n".encode())
                print(f"LYRX: {ls_y}:{rs_x}")
            if abs(j.get_axis(0)) >0:
                ls_x = math.floor(j.get_axis(0) * 255)
                ser.write(f"LSX:{ls_x}\n".encode())
                print(f"LSX: {ls_x}")
            if j.get_axis(4) > -1:
                r2_a = math.floor((j.get_axis(4) + 1)*30/2)
                ser.write(f"R2A:{r2_a}\n".encode())
                print(f"R2A: {r2_a}")
            if j.get_axis(3) > -1:
                l2_a = math.floor((j.get_axis(3) + 1)*30/2)
                ser.write(f"L2A:{l2_a}\n".encode())
                print(f"L2A: {l2_a}")
                      
    time.sleep(0.05)
