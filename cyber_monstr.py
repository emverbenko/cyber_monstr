import socket

SERVER = 'localhost'
PORT = 5555

start_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start_socket.connect((SERVER, PORT))

while True:
    print('Введите пароль:')
    player_key = input()
    start_socket.send(player_key.encode())
    status = start_socket.recv(1024)
    print(status.decode('utf-8'))
    if status.decode('utf-8') == 'Пароль верный! Внимание! Активация кибер монстра!':
        break
start_socket.close()
