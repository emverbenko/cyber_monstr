import socket

SERVER = 'localhost'
PORT = 5555

KEY = 55749

start_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start_socket.connect((SERVER, PORT))

while True:
    print('Введите пароль:')
    player_key = input()
    start_socket.send(player_key.encode())
    print(conn)
response = start_socket.recv(1024)
start_socket.close()