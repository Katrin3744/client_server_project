import socket
from ENTRANCE import for_start

_entrances = {}
for_start(_entrances)
HOST = _entrances['S_HOST']
PORT = int(_entrances['S_PORT'])
server = HOST, PORT
flg = ''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while flg != 'OK':
        address = input()
        text = input()
        s.sendto((address + '/' + text).encode('utf-8'), server)
        data1 = s.recv(1024)
        flg = data1.decode('utf-8')
        print(flg)
        if flg == 'OK':
            break

print('Received', data1.decode('utf-8'))
