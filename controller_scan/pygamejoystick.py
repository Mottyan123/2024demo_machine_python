import pygame
import sys

# Pygameの初期化
pygame.init()

# ジョイスティックの初期化
pygame.joystick.init()

# ジョイスティックが接続されているか確認
if pygame.joystick.get_count() == 0:
    print("ジョイスティックが接続されていません")
    sys.exit()

# 最初のジョイスティックを取得
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"ジョイスティックの名前: {joystick.get_name()}")
print(f"ジョイスティックのボタンの数: {joystick.get_numbuttons()}")
print(f"ジョイスティックの軸の数: {joystick.get_numaxes()}")

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # ジョイスティックの軸の値を取得
        if event.type == pygame.JOYAXISMOTION:
            left_stick_x = joystick.get_axis(0)
            left_stick_y = joystick.get_axis(1)
            right_stick_x = joystick.get_axis(2)
            right_stick_y = joystick.get_axis(5)
            print(f"左スティック - X軸: {left_stick_x:.2f}, Y軸: {left_stick_y:.2f}")
            print(f"右スティック - X軸: {right_stick_x:.2f}, Y軸: {right_stick_y:.2f}")

    pygame.time.wait(100)  # 少し待機してから再度ループ

pygame.quit()
