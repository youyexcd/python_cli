#!/user/bin/env python
# -*- coding:utf-8 -*-


import socket
import json


def connect_to_server(host, port):
    s = socket.socket()
    s.connect((host, port))
    return s

def recieve_to_json(data):
    return json.loads(data.decode('utf-8').replace('\'', '\"'))


s = connect_to_server('127.0.0.1', 1234)
recv_data = s.recv(1024)
host_info = recieve_to_json(recv_data)
while True:
    # 待发送的信息
    send_data = input('[%s]># ' % host_info['host_name']).strip()
    s.send(bytes(send_data, encoding='utf-8'))
#    print('等待对方回复:')

    recv_data = s.recv(1024)
    print(str(recv_data, encoding='utf-8'))
s.close()
