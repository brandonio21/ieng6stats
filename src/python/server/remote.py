from service import ServerStatService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
def main():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = ServerStatService.Client(protocol)

    transport.open()
    print(client.ping())
    transport.close()


if __name__ == '__main__':
    main()
