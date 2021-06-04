import smtplib
import uuid
import socket

from ENTRANCE import for_start

_entrances = {}
for_start(_entrances)
smtp_host = _entrances['SMTP_HOST']  # google
ad_mail = _entrances['ADMIN_MAIL']
password = _entrances['ADMIN_PASSWORD']
_entrances = {}
for_start(_entrances)
YA_HOST = _entrances['S_HOST']
YA_PORT = int(_entrances['S_PORT'])


def send_mail(msg, to):
    with smtplib.SMTP(smtp_host, int(_entrances['SMTP_PORT'])) as smtp:
        smtp.starttls()
        smtp.login(ad_mail, password)
        smtp.sendmail(ad_mail, to, msg)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((YA_HOST, YA_PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        while True:
            email, text = data.decode().split('/')
            if '@' and '.' not in email:
                conn.sendall(b'Error')
            else:
                user_id = uuid.uuid4()
                ID = 'ID' + str(addr[0]) + '/' + email + '/' + str(user_id)
                conn.sendall(b'OK')
                send_mail('Subject:' + ID + '\n' + text, ad_mail)
                send_mail('Subject:' + ID, email)
                break
