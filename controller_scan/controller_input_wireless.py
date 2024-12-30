import pygame
import time
import socket
import math
def sendMessage(message):
    message += "\n"#文末に改行コードを追加
    client.sendall(bytes(message, encoding='ASCII'))#文字列をバイトに変換し送信（文字コードはASCIIを使用）
    print("サーバーへデータ送信")
#pygame初期化部分
pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
print("pygame初期化完了")
#wifi設定部分
ip_address = '192.168.137.55' #サーバー（ESP32のIPアドレス）
port = 5000 #ポート番号
buffer_size = 4092 #一度に受け取るデータの大きさを指定
conection_status = False
try:
    #クライアント用インスタンスを生成
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # サーバーに接続を要求する（IPアドレスとポート番号を指定）
    client.connect((ip_address, port))
    while conection_status == False: #ESP32との接続が確立されるまで続ける
        data = client.recv(buffer_size) #サーバから送られてきたデータを読み取り（上限4092ビット）
        if data.decode() == "ready": #ESP32から接続完了の合図を受け取ったら
            conection_status = True #Trueに変更しループから出る
            print("サーバとの接続完了")
    print("コントローラーを操作してください")
    while True:#以下ループ
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN: #ボタンが押された場合
                if event.button == 1:
                    print("バツボタンが押されました")
                    events = pygame.event.get()
                    print(math.floor(j.get_button(1)))
                    sendMessage("XB:"+str(math.floor(j.get_button(1))))
                    time.sleep(0.05)
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 1:
                    print("バツボタンが離されました")
                    events = pygame.event.get()
                    print(math.floor(j.get_button(1)))
                    sendMessage("XB:"+str(math.floor(j.get_button(1))))
                    time.sleep(0.05)
            elif event.type == pygame.JOYAXISMOTION:
                if abs(j.get_axis(5)) > 0 or abs(j.get_axis(1)) > 0 or j.get_axis(4) > -1 or j.get_axis(3) > -1:
                    events = pygame.event.get()
                    print("RSY",math.floor(j.get_axis(5)*255) ,"LSY",math.floor(j.get_axis(1)*255),"R2A", math.floor((j.get_axis(4)+1)*255/2) ,"L2A", math.floor((j.get_axis(3)+1)*255/2))
                    sendMessage("RSY:"+str(math.floor(((j.get_axis(5)*180)+180)*0.5)))
                    sendMessage("LSY:"+str(math.floor(((j.get_axis(1)*180)+180)*0.5)))
                    sendMessage("R2A:"+str(math.floor((j.get_axis(4)+1)*255/2)))
                    sendMessage("L2A:"+str(math.floor((j.get_axis(3)+1)*255/2)))
                             
except KeyboardInterrupt:
    sendMessage("exit")
    client.close()
    print("ソケット通信を終了")
    print("プログラムを終了します")
    j.quit()
