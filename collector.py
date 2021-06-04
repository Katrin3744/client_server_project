import email
from ENTRANCE import for_start
import time
from imaplib import IMAP4_SSL


def getMsgs(_mes):
    with IMAP4_SSL(YA_HOST, YA_PORT) as s:
        s.login(YA_USER, YA_PASSWORD)
        s.select()
        _, data = s.search(None, 'ALL')
        for num in data[0].split():
            _, data = s.fetch(num, '(RFC822)')
            raw = data[0][1]
            mail = email.message_from_bytes(raw)

            if not mail['Subject'] in _mes.keys():
                _mes[mail['Subject']] = mail.get_payload()


def for_errors(_mes):
    arr_line = []
    try:
        with open(r'C:\Users\Кухаренко Екатерина\PycharmProjects\pythonProject9\error_request.log', 'r') as file:
            arr_line = file.readlines()
    finally:
        with open('error_request.log', 'a') as file:
            for i in _mes.keys():
                flg = True
                for j in arr_line:
                    if i in j:
                        flg = False
                if not i.startswith('ID') and flg:
                    file.write('\n' + i + '\n' + str(_mes[i]))


def for_success(_mes):
    lines = []
    try:
        with open('success_request.log', 'r') as file:
            lines = file.readlines()
    finally:
        with open('success_request.log', 'a') as file:
            for i in _mes.keys():
                flg = True
                for line in lines:
                    if i in line:
                        flg = False
                if i.startswith('ID') and flg:
                    file.write('\n' + i + '\n' + _mes[i])


massages = {}
_entrances = {}
for_start(_entrances)
YA_HOST = _entrances['IMAP_HOST']
YA_PORT = int(_entrances['IMAP_PORT'])
YA_USER = _entrances['ADMIN_MAIL']
YA_PASSWORD = _entrances['ADMIN_PASSWORD']
time_t = int(_entrances['PERIOD_CHECK'])

while True:
    getMsgs(massages)
    print(massages)
    for_success(massages)
    for_errors(massages)
    time.sleep(time_t)
