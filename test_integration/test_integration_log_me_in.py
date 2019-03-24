import time

import pytest

from logmein.logmein import Logmein


class TestIntegrationLogmein:
    def setup_method(self):
        self.logmein = Logmein('127.0.0.1', 5005, 2000)
        self.logmein.initialize('test_data/test_sip_registrations.txt')
        self.logmein.start_server_in_thread()
        self.logmein.connect()

    def test_connect_and_disconnect(self):
        pass

    def test_sip_registration(self):
        assert self.logmein.sip_registrations
        assert len(self.logmein.sip_registrations) == 2
        sip_registration = self.logmein.get_sip_registration(b'dummyAddressOfRecord')
        assert sip_registration

    def test_answer_sip_registrations(self):
        sip_registration = self.logmein.query('dummyAddressOfRecord')
        assert sip_registration == '{"tenantId": "dummyTenantId", "uri": "dummyUri", "contact": "dummyContact", "path": ["dummyPath"], "source": "dummySource", "target": "dummyTarget", "userAgent": "dummyUserAgent", "rawUserAgent": "dummyRawUserAgent", "created": "dummyCreated", "lineId": "dummyLineId"}'

    def test_when_address_of_record_not_found_then_return_empty_string(self):
        sip_registration = self.logmein.query('addressOfRecordThatDoesNotExist')
        assert sip_registration == ''

    def test_when_connection_inactive_for_10_seconds_then_close_connection(self):
        time.sleep(11)
        with pytest.raises(ConnectionAbortedError):
            self.logmein.query('dummyAddressOfRecord')

    def test_reconnection_after_connection_timeout(self):
        time.sleep(11)
        with pytest.raises(ConnectionAbortedError):
            self.logmein.query('dummyAddressOfRecord')
        self.logmein.disconnect()
        self.logmein.initialize_socket_to_server()
        self.logmein.connect()
        self.logmein.query('dummyAddressOfRecord')

    def teardown_method(self):
        self.logmein.disconnect()
        self.logmein.stop_server()
