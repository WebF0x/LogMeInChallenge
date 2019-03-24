from logmein.logmein import Logmein


def main():
    print('Initializing')
    logmein = Logmein()
    logmein.initialize('sipRegistrations.txt')
    print('Starting server')
    logmein.start_server_in_thread()
    print('Connecting to server')
    logmein.connect()
    while True:
        address_of_record = input('Address of record? (Empty to quit)')
        if not address_of_record:
            break
        print(f'Querying with address of record = "{address_of_record}"')
        sip_registration = logmein.query(address_of_record)
        print(sip_registration)
    print('Disconnecting from server')
    logmein.disconnect()
    print('Stopping server')
    logmein.stop_server()
    print('Bye bye!')


if __name__ == '__main__':
    main()
