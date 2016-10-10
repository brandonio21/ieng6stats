from handler import ServerStatServiceHandler
from service import ServerStatService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from jsonproxy import JSONDatabaseProxy
from daemon import ServerStatDaemon

import threading

def launch_daemon(*args):
    daemon = ServerStatDaemon(args[0])
    daemon.loop()

def main():
    proxy = JSONDatabaseProxy('data')
    handler = ServerStatServiceHandler(proxy)
    processor = ServerStatService.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, 
                                     tfactory, pfactory)

    daemon_thread = threading.Thread(target=launch_daemon, args=[proxy])
    daemon_thread.start()
    print("Serving requests on port 9090")
    server.serve()

if __name__ == '__main__':
    main()
