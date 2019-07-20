import os
import sys
from core.server import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == '__main__':
    s = SocketServer()
    s.run()