import socket
def send_commands(msg):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as rakwan_socket:
        rakwan_socket.connect(('localhost',12345))
        rakwan_socket.sendall(msg.encode('utf-8'))
        if __name__ == '__main__':
            send_commands('')