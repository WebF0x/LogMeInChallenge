import json
import socket
import threading

from logmein.sip_registrations import open_file, parse_sip_registrations
from logmein.tcp_server import TcpServer


class Logmein:
    def __init__(self):
        self.tcp_ip = '127.0.0.1'
        self.tcp_port = 5005
        self.server_message_size = 2000
        self.server = TcpServer(self.tcp_ip, self.tcp_port, self.server_message_size)
        self.server_thread = None
        self.socket = None
        self.sip_registrations = None

    def start_server_in_thread(self):
        self.server_thread = threading.Thread(target=self.server.start_listening)
        self.server_thread.start()
        while not self.server.is_running:
            pass

    def initialize_socket_to_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(1)

    def connect(self):
        self.socket.connect((self.tcp_ip, self.tcp_port))
        while not self.server.is_connected:
            pass

    def disconnect(self):
        self.socket.close()
        while self.server.is_connected:
            pass

    def initialize_sip_registrations(self, sip_registractions_file):
        sip_registrations_string = open_file(sip_registractions_file)
        self.sip_registrations = parse_sip_registrations(sip_registrations_string)

    def get_sip_registration(self, encoded_address_of_record):
        address_of_record = encoded_address_of_record.decode('utf-8')
        if address_of_record not in self.sip_registrations:
            return b'NotFound'
        sip_registration_json = self.sip_registrations[address_of_record]
        sip_registration = json.dumps(sip_registration_json)
        return sip_registration.encode('utf-8')

    def initialize(self, sip_registractions_file):
        self.initialize_socket_to_server()
        self.initialize_sip_registrations(sip_registractions_file)
        self.server.do_work = self.get_sip_registration

    def query(self, address_of_record):
        assert address_of_record
        encoded_address_of_record = address_of_record.encode('utf-8')
        self.socket.send(encoded_address_of_record)
        response = self.socket.recv(self.server_message_size)
        if response == b'NotFound':
            return ''
        return response.decode('utf-8')

    def stop_server(self):
        self.server.stop_listening()
        self.server_thread.join()
