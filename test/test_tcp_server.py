import socket
import threading

from logmein.tcp_server import TcpServer


class TestTcpServer:
    def setup_method(self):
        tcp_ip = '127.0.0.1'
        tcp_port = 5005
        self.server_message_size = 50
        self.server = TcpServer(tcp_ip, tcp_port, self.server_message_size)
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

    def test_server_does_work(self):
        self.connect()

        def do_work_spy(data_received_by_server):
            assert data_received_by_server == b'data received by server'
            return b'data sent by server'

        self.server.do_work = do_work_spy
        self.socket.send(b'data received by server')
        while self.socket.recv(self.server_message_size) != b'data sent by server':
            pass
        self.disconnect()

    def test_server_does_work_multiple_times(self):
        self.connect()

        def do_work_spy(data_received_by_server):
            if data_received_by_server == b'data received by server 1':
                return b'data sent by server 1'
            if data_received_by_server == b'data received by server 2':
                return b'data sent by server 2'
        self.server.do_work = do_work_spy
        self.socket.send(b'data received by server 1')
        while self.socket.recv(self.server_message_size) != b'data sent by server 1':
            pass
        self.socket.send(b'data received by server 2')
        while self.socket.recv(self.server_message_size) != b'data sent by server 2':
            pass
        self.disconnect()

    def teardown_method(self):
        assert self.server.is_running
        self.server.stop_listening()
        while self.server.is_connected:
            pass
        while self.server.is_running:
            pass
        self.server_thread.join()
