import socket
import threading

USERNAME = ''


def listen_server(sock):
    while True:
        try:
            msg = sock.recv(2048)
            print(msg.decode())
        except Exception as e:
            print(e)
            sock.close()


def start_client(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 1234))
    threading.Thread(target=listen_server, args=[sock]).start()
    print('Connect to chat!')
    sock.send(bytes('[' + USERNAME + '] join to the chat', 'utf-8'))
    while True:
        msg = str(input())
        sock.send(bytes('[' + USERNAME + '] -> ' + msg, 'utf-8'))


if __name__ == '__main__':
    host = str(input('Please enter server ip: '))
    USERNAME = str(input('Enter your name: '))
    start_client(host)
