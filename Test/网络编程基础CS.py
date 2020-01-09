"""
server.py
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址和端口
s.bind(('192.168.31.108',8001))
#设定半连接池的数量
s.listen(5)
print('等待客户连接...')
#阻塞等待客户端连接
connect,addr=s.accept()
#接受消息（都是二进制）
msg=connect.recv(1024)
print('收到客户端的消息：',msg.decode('utf-8'))
#发送消息
connect.send(bytes('我收到啦',encoding='utf-8'))

#关闭连接
connect.close()
s.close()



"""
client.py
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址和端口
s.connect(('192.168.31.108',8001))
#发送消息
s.send(bytes('hello socket',encoding='utf-8'))
#接受消息
msg=s.recv(1024)
print('收到客户端的消息：',msg.decode('utf-8'))
#关闭连接
s.close()
