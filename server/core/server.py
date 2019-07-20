import socket
import struct

from conf.settings import *
from concurrent.futures import ThreadPoolExecutor


class SocketServer():
    def __init__(self):
        # 创建socket开始监听
        self.soc = socket.socket()
        self.soc.bind((SERVER_IP, SERVER_PORT))
        self.soc.listen(5)
        # 生成线程池
        self.poll = ThreadPoolExecutor(1000)
        print("server listening...")

    # 与客户端交互
    def client_handler(self, client):
        while 1:
            data = self.__recv_request(client)

    # 接受客户端连接
    def run(self):
        while 1:
            client, addr = self.soc.accept()
            print("client connect %s" % addr[0])
            self.poll.submit(self.client_handler, client)

    # 接受客户端请求数据
    def __recv_request(self, client):
        # 先收长度
        len_bytes = client.recv(4)
        l = struct.unpack("i", len_bytes)[0]

        # 收数据
        data_bytes = client.recv(l)
        data = data_bytes.decode("utf-8")
        print("收到一个数据", data)
        return data
