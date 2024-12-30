import pygame
#import serial
import time
pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
print("コントローラのボタンを押してください")
#ser = serial.Serial("COM9",115200,timeout=0.1)
time.sleep(2)

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN: #ボタンが押された場合
                if event.button == 0:
                    print("0")
                    #ser.write(f"SB:{1}\n".encode())
                    time.sleep(0.1)
                if event.button == 1:
                    print("1")
                    #ser.write(f"XB:{1}\n".encode())
                    time.sleep(0.1)
                if event.button == 2:
                    print("2")
                    time.sleep(0.1)
                if event.button == 3:
                    print("3")
                    time.sleep(0.1)
                if event.button == 4:
                    print("4")
                    time.sleep(0.1)
                if event.button == 5:
                    print("5")
                    time.sleep(0.1)
                if event.button == 6:
                    print("6")
                    time.sleep(0.1)
                if event.button == 7:
                    print("7")            
                    time.sleep(0.1)
                if event.button == 8:
                    print("8")
                    time.sleep(0.1)
                if event.button == 9:
                    print("9")
                    time.sleep(0.1)
                if event.button == 10:
                    print("10")
                    time.sleep(0.1)
                if event.button == 11:
                    print("11")
                    time.sleep(0.1)
                if event.button == 12:
                    print("12")
                    time.sleep(0.1)
                if event.button == 13:
                    print("13")
                    time.sleep(0.1)
                if event.button == 14:
                    print("14")
                    time.sleep(0.1)
                if event.button == 15:
                    print("15")
                    time.sleep(0.1)
            # if event.type == pygame.JOYBUTTONUP: #ボタンが離された場合
            #     if event.button == 0:
            #         print("□ボタンが離されました")
            #         #ser.write(f"SB:{0}\n".encode())
            #         time.sleep(0.1)
            if event.type == pygame.JOYHATMOTION: #十字キーが入力場合
                print("十字キー座標")
                print("("+str((j.get_hat(0))[0])+","+str((j.get_hat(0))[1])+")")
            if event.type == pygame.JOYAXISMOTION: #スティックが入力された場合
                if abs((j.get_axis(0))) > 0.25:
                    print(f"0: {j.get_axis(0)}")
                if abs((j.get_axis(1))) > 0.25:
                    print(f"1: {j.get_axis(1)}")
                if abs((j.get_axis(2))) > 0.25:
                    print(f"2: {j.get_axis(2)}")
                if abs((j.get_axis(3))) > 0.25:
                    print(f"3: {j.get_axis(3)}")
                if (j.get_axis(4)) > -1.00:
                    print(f"4: {j.get_axis(4)}")
                if (j.get_axis(5)) > -1.00:
                    print(f"5: {j.get_axis(5)}")
                                                  
except KeyboardInterrupt:
    print("プログラムを終了します")
    j.quit()