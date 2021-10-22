import socket, threading
CLIENTS = []


def close_connect(client):
    if client in CLIENTS:
        client.close()
        CLIENTS.remove(client)
        print(CLIENTS)


def listen_user(client, addr):
    while True:
        try:
            msg = client.recv(2048)
            if msg:
                print(addr[1], '->', msg.decode())
                broadcast(msg, client)
            else:
                close_connect(client)
                break
        except Exception as e:
            print(e)
            close_connect(client)
            break


def broadcast(msg, client):
    for cl in CLIENTS:
        try:
            if cl != client:
                cl.send(msg)
        except Exception as e:
            print(e)
            close_connect(client)


def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 1234))
    sock.listen(5)
    print('server started!')

    while True:
        client, addr = sock.accept()
        if client not in CLIENTS:
            CLIENTS.append(client)
        threading.Thread(target=listen_user, args=[client, addr]).start()


if __name__ == '__main__':
    start_server()
