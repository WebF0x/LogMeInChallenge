from logmein.logmein import Logmein


def main():
    print('Initializing')
    logmein = Logmein('127.0.0.1', 5005, 2000)
    logmein.initialize('sipRegistrations.txt')
    print('Starting server')
    logmein.start_server_in_thread()
    print('Connecting to server')
    logmein.connect()
    while True:
        address_of_record = input('Address of record? (Empty to quit): ')
        if not address_of_record:
            break
        print(f'Querying with address of record = "{address_of_record}"')
        try:
            sip_registration = logmein.query(address_of_record)
        except ConnectionAbortedError:
            print('Got disconnected from the server')
            has_to_reconnect_and_continue = input('Would you like to reconnect and continue? y/n: ').lower() == 'y'
            if has_to_reconnect_and_continue:
                print('Reconnecting to server')
                logmein.disconnect()
                logmein.initialize_socket_to_server()
                logmein.connect()
                continue
            else:
                break
        print(sip_registration)
    print('Disconnecting from server')
    logmein.disconnect()
    print('Stopping server')
    logmein.stop_server()
    print('Bye bye!')


if __name__ == '__main__':
    main()
