"""
基于TCP和UDP的编程例子
Date:2020.1.9
"""
#----------------------------------基于TCP-------------------------
#服务端
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

#客户端
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

#----------------------------------基于UDP-------------------------
#服务端
import socket

ip_port=('192.168.31.108',8000)
#创建客户端的套接字(数据报的方式,基于TCP的套接字是数据流的方式)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(ip_port)
print('等待客户端...')

msg,addr=s.recvfrom(1024)
print('收到客户端的消息：',msg)
s.sendto(bytes('我收到你的消息啦',encoding='utf-8'),addr) #返回给客户端时，发送消息只需要addr

#客户端
import socket

ip_port=('192.168.31.108',8000)
#创建客户端的套接字(数据报的方式,基于TCP的套接字是数据流的方式)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(bytes('hello UDP',encoding='utf-8'),ip_port) #发送给客户端消息时，需要ip_addr
msg,addr=s.recvfrom(1024)
print('收到服务端的消息：',msg.decode('utf-8'))
