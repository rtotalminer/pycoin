from pycoin.src.net.server import *

endpoint = TCP4ServerEndpoint(reactor, 5999)
endpoint.listen(MyFactory())

