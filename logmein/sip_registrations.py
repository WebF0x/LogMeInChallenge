import json


def open_file(file_path):
    with open(file_path) as file:
        return file.read()


def parse_sip_registrations(sip_registrations_string):
    lines_with_extra_empty_line = sip_registrations_string.split('\n')
    lines = lines_with_extra_empty_line[:-1]
    records_json_without_address = [json.loads(line) for line in lines]
    addresses_of_record = [record_json.pop('addressOfRecord') for record_json in records_json_without_address]
    return {
        addresses_of_record[i]: line_json
        for i, line_json in enumerate(records_json_without_address)
    }
