"""
TCP协议实现模拟远程访问服务器并执行命令
Date:2020.1.11
"""
#----------------------------------------------------
import socket
import subprocess

ip_port=('192.168.31.108',8000)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ip_port)
s.listen(5)
while True:
    print('waitting...')
    connect,addr=s.accept()
    print(connect,addr)
    while True:
        msg=connect.recv(1024)
        print ('received cmd:{msg} from {addr}'.format(msg=msg.decode('utf-8'),addr=addr))
        if msg==b'quit':
            print('-----break link-----')
            connect.close()
            break
        res=subprocess.Popen(msg.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        err=res.stderr.read()
        if err:
            cmd_res=err
        else:
            cmd_res=res.stdout.read()
        connect.send(cmd_res)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.31.108', 8000))

while True:
    msg=input('请输入远程命令:').strip()
    if not msg:continue
    if msg=='quit':
        s.send(bytes(msg, encoding='utf-8'))
        break
    s.send(bytes(msg, encoding='utf-8'))
    msg = s.recv(1024)
    print('收到服务端执行结果：\n', msg.decode('gbk'))
    # 关闭连接
s.close()
