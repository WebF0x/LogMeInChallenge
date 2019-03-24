import socket


class TcpServer(object):
    def __init__(self, tcp_ip, tcp_port, buffer_size):
        self.tcp_ip = tcp_ip
        self.tcp_port = tcp_port
        self.buffer_size = buffer_size
        self.is_running = False
        self.is_connected = False

    def start_listening(self):
        self.is_running = True
        socket_to_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_to_client.bind((self.tcp_ip, self.tcp_port))
        socket_to_client.listen(1)
        socket_to_client.settimeout(0.1)
        while self.is_running:
            try:
                connection, address = socket_to_client.accept()
            except socket.timeout:
                continue
            self.is_connected = True
            while self.is_running:
                data = connection.recv(self.buffer_size)
                if not data:
                    break
                connection.send(data)
            connection.close()
            self.is_connected = False

    def stop_listening(self):
        self.is_running = False
