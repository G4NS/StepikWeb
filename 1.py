import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind(('0.0.0.0', 2222))
socket.listen(10)

while True:
    connect, addr = socket.accept()
    while True:
        data = connect.recv(1024)
        if str(data) == 'close':
            break

        connect.send(data)
        connect.close()