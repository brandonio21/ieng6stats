from handler import ServerStatServiceHandler
from service import ServerStatService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

def main():
    handler = ServerStatServiceHandler(None)
    processor = ServerStatService.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, 
                                     tfactory, pfactory)
    print("Serving requests on port 9090")
    server.serve()

if __name__ == '__main__':
    main()