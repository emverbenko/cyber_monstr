import socket

SERVER = 'localhost'
PORT = 5555

KEY = 557497654398

start_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start_socket.bind((SERVER, PORT))
start_socket.listen(2)
conn, addr = start_socket.accept()

right_key = str.encode('Пароль верный! Внимание! Активация кибер монстра!')
wrong_key = str.encode('Неверный пароль! Пожалуста введите пароль ещё раз!')

while True:
    response = conn.recv(1024)
    if int(response.decode('utf-8')) == KEY:
        conn.send(right_key)
    else:
        conn.send(wrong_key)
conn.close()
