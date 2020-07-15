import socket
import select
import time

"""
Date：2010-7-15
select实现多路IO复用：监听多连接
"""

server=socket.socket()
server.bind(('192.168.133.1',8002))
server.listen(5)
inputs=[server,]
while True:
    r,w,e=select.select(inputs,[],[],5) #内核进行监听并获取数据
    
    #数据拷贝到用户态
    for i in r:
        if i == server:#如果server触发，则说明有新的客户端尝试连接
            conn,addr=i.accept()
            #msg = conn.recv(1024)
            print('Sever触发...:有客户端加入--->',addr)
            inputs.append(conn)
        else:           #说明是监听列表inputs中的某个conn对象触发，则也就是说连接的某一段发消息了
            msg = i.recv(1024)
            print('Conn触发...：有客户的发来消息--->',msg.decode('utf-8'))
            i.send('收到啦...'.encode('utf-8'))
    print('Waiting...')
    time.sleep(1)


#--------------------------------------------------------------
import socket
import select
import time
client=socket.socket()
client.connect(('192.168.133.1',8002))
while 1:
    data = input('请输入要发送的消息：')
    client.send(data.encode('utf-8'))
    msg = client.recv(1024)
    print('来自Server端的消息：',msg.decode('utf-8'))
    time.sleep(1)

    
        


