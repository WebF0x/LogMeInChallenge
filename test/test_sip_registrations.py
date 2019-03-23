import pytest

from logmein.sip_registrations import open_file, parse_sip_registrations


def test_open_file_raises_when_does_not_exist():
    file_path = 'thisFileDoesNotExist.txt'
    with pytest.raises(FileNotFoundError):
        open_file(file_path)


def test_open_file_returns_file_content():
    file_path = 'test_data/testFileContainingHelloWorldOnTwoLines.txt'
    file_content = open_file(file_path)
    assert file_content == 'hello\nworld'


def test_load_sip_registrations_skips_the_last_empty_line():
    sip_registrations_string = open_file('test_data/test_sip_registrations.txt')
    sip_registrations = parse_sip_registrations(sip_registrations_string)
    assert len(sip_registrations) == 2
    assert 'dummyAddressOfRecord' in sip_registrations
    assert 'dummyAddressOfRecord2' in sip_registrations


def test_load_sip_registrations_data_correctly():
    sip_registrations_string = open_file('test_data/test_sip_registrations.txt')
    sip_registrations = parse_sip_registrations(sip_registrations_string)
    sip_registration_1 = sip_registrations['dummyAddressOfRecord']
    sip_registration_2 = sip_registrations['dummyAddressOfRecord2']
    assert sip_registration_1['tenantId'] == 'dummyTenantId'
    assert sip_registration_1['uri'] == 'dummyUri'
    assert sip_registration_1['contact'] == 'dummyContact'
    assert sip_registration_1['path'] == ['dummyPath']
    assert sip_registration_1['source'] == 'dummySource'
    assert sip_registration_1['target'] == 'dummyTarget'
    assert sip_registration_1['userAgent'] == 'dummyUserAgent'
    assert sip_registration_1['rawUserAgent'] == 'dummyRawUserAgent'
    assert sip_registration_1['created'] == 'dummyCreated'
    assert sip_registration_1['lineId'] == 'dummyLineId'
    assert sip_registration_2['tenantId'] == 'dummyTenantId2'
    assert sip_registration_2['uri'] == 'dummyUri2'
    assert sip_registration_2['contact'] == 'dummyContact2'
    assert sip_registration_2['path'] == ['dummyPath2']
    assert sip_registration_2['source'] == 'dummySource2'
    assert sip_registration_2['target'] == 'dummyTarget2'
    assert sip_registration_2['userAgent'] == 'dummyUserAgent2'
    assert sip_registration_2['rawUserAgent'] == 'dummyRawUserAgent2'
    assert sip_registration_2['created'] == 'dummyCreated2'
    assert sip_registration_2['lineId'] == 'dummyLineId2'

