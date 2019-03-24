import socket
import threading

from logmein.tcp_server import TcpServer


class TestTcpServer:
    def setup_method(self):
        tcp_ip = '127.0.0.1'
        tcp_port = 5005
        buffer_size = 20
        self.server = TcpServer(tcp_ip, tcp_port, buffer_size)
        assert not self.server.is_running
        assert not self.server.is_connected
        self.server_thread = threading.Thread(target=self.server.start_listening)
        self.server_thread.start()
        while not self.server.is_running:
            pass
        assert not self.server.is_connected
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5)

    def connect(self):
        tcp_ip = '127.0.0.1'
        tcp_port = 5005
        self.socket.connect((tcp_ip, tcp_port))
        while not self.server.is_connected:
            pass

    def disconnect(self):
        self.socket.close()
        while self.server.is_connected:
            pass

    def test_test_fixtures(self):
        pass

    def test_connect_to_server(self):
        assert not self.server.is_connected
        self.connect()
        assert self.server.is_connected
        self.disconnect()
        assert not self.server.is_connected

    def teardown_method(self):
        assert self.server.is_running
        self.server.stop_listening()
        while self.server.is_connected:
            pass
        while self.server.is_running:
            pass
        self.server_thread.join()
