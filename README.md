# LogMeInChallenge

## Example of output
```
Initializing
Starting server
Connecting to server
Address of record? (Empty to quit): this is a bad address
Querying with address of record = "this is a bad address"

Address of record? (Empty to quit): 014e9cc9ea34446a2b000100620005
Querying with address of record = "014e9cc9ea34446a2b000100620005"
{"tenantId": "0127d974-f9f3-0704-2dee-000100420001", "uri": "sip:014e9cc9ea34446a2b000100620005@193.68.97.166;jbcuser=cpe70", "contact": "<sip:014e9cc9ea34446a2b000100620005@65.237.236.107;jbcuser=cpe70>;methods=\"INVITE, ACK, BYE, CANCEL, OPTIONS, INFO, MESSAGE, SUBSCRIBE, NOTIFY, PRACK, UPDATE, REFER\"", "path": ["<sip:Mi0xOTkuMTkyLjE2NS4xOTQtMTk2MjI@74.144.114.94:5060;lr>"], "source": "45.244.97.230:19622", "target": "192.250.34.27:5061", "userAgent": "polycom.soundstationip.5000", "rawUserAgent": "PolycomSoundStationIP-SSIP_5000-UA/199.152.0.142", "created": "2016-12-12T22:42:04.538Z", "lineId": "0148b27e-1149-a336-b632-000100620005"}
Address of record? (Empty to quit): 014e9cc9ea34446a2b000100620005
Querying with address of record = "014e9cc9ea34446a2b000100620005"
Got disconnected from the server
Would you like to reconnect and continue? y/n: y
Reconnecting to server
Address of record? (Empty to quit): 014e9cc9ea34446a2b000100620005
Querying with address of record = "014e9cc9ea34446a2b000100620005"
{"tenantId": "0127d974-f9f3-0704-2dee-000100420001", "uri": "sip:014e9cc9ea34446a2b000100620005@193.68.97.166;jbcuser=cpe70", "contact": "<sip:014e9cc9ea34446a2b000100620005@65.237.236.107;jbcuser=cpe70>;methods=\"INVITE, ACK, BYE, CANCEL, OPTIONS, INFO, MESSAGE, SUBSCRIBE, NOTIFY, PRACK, UPDATE, REFER\"", "path": ["<sip:Mi0xOTkuMTkyLjE2NS4xOTQtMTk2MjI@74.144.114.94:5060;lr>"], "source": "45.244.97.230:19622", "target": "192.250.34.27:5061", "userAgent": "polycom.soundstationip.5000", "rawUserAgent": "PolycomSoundStationIP-SSIP_5000-UA/199.152.0.142", "created": "2016-12-12T22:42:04.538Z", "lineId": "0148b27e-1149-a336-b632-000100620005"}
Address of record? (Empty to quit): 
Disconnecting from server
Stopping server
Bye bye!
```

## Run it yourself

```
git clone https://github.com/WebF0x/LogMeInChallenge.git
cd LogMeInChallenge
python main.py
```
