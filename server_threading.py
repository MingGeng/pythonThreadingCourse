import threading
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

ADDR = ('', 1234)
BUFSIZ = 1024
tcp_server_sock = socket(AF_INET, SOCK_STREAM)
tcp_server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server_sock.bind(ADDR)
tcp_server_sock.listen()

def handle(sock, addr):
    while True:
        data = sock.recv(BUFSIZ).decode()
        if not data:
            sock.close()
            break
        print('?????{}'.format(data))
        sock.send(
            '[{}] {}'.format('ShiYanLou', data).encode())
    sock.close()
    print('{} ???'.format(addr))

def main():
    print('???????...')
    while True:
        try:
            tcp_extension_sock, addr = tcp_server_sock.accept()
        except KeyboardInterrupt:
            break
        t = threading.Thread(
            target=handle, args=(tcp_extension_sock, addr))
        t.start()
    print('\nExit')
    tcp_server_sock.close()

if __name__ == '__main__':
    main()
