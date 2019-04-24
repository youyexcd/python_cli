#!/user/bin/env python
# -*- coding:utf-8 -*-

import socket

s = socket.socket()
host = '127.0.0.1'
port = 1234
s.bind((host, port))
s.listen(1)

while True:
    con, addr = s.accept()
    if con is not None:
        print('客户端已经连接,\n.')
        host_info = """{'host_name': 'Socket Server'}"""
        con.send(bytes(host_info, encoding='utf-8'))
    while True:
        try:
            recv_data = con.recv(1024)
            # 显示接收的信息
            print('对方发送的信息：', str(recv_data, encoding='utf-8'))
            send_data = input('我回复>>').strip()
            con.send(bytes(send_data, encoding='utf-8'))
            print('等待对方发送信息>>')
        except Exception:
            print('远程主机强迫关闭了一个现有的连接，续继等待其它的连接。')
            break
    con.close()

