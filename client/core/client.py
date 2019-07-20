import socket
from conf.settings import *


class Client:
    def __init__(self):
        self.soc = socket.socket()
        # 可以自定义服务器的IP，端口
        ip = input("host: ").strip()
        if not ip:
            self.soc.connect((SERVER_IP, SERVER_PORT))
        else:
            self.soc.connect((ip, SERVER_PORT))
        print("connected to server!")

    def login(self, args):
        print("login run")
        pass

    def register(self, args):
        pass

    def run(self):
        while 1:
            cmd = input("cmd: ").strip()
            args = cmd.split()
            # 判断指令是否支持
            if hasattr(self, args[0]):
                getattr(self, args[0])(args[1:])  # 取后面的参数
            else:
                print("command not found.")
