from .servertrak import servertrak
from .servertrak.common.server import Server
from .servertrak.common.output import JSONOutput
from .servertrak.common.user import User
from .servertrak.proxies.ssh import SSHProxy
import time
from datetime import datetime

class ServerStatDaemon(object):
    def __init__(self, dbproxy):
        self.dbproxy = dbproxy


    def loop(self):

        discoverable_hostname_pattern = 'ieng6(-2[0-9][0-9])?\.ucsd\.edu'
        hostnames = set(servertrak.generate_servers_from_regex(discoverable_hostname_pattern))

        proxy = SSHProxy()
        servers = [Server(hostname) for hostname in hostnames]
        users = [User('bmilton', ['*.ucsd.edu'])]
        command = 'uptime'
        output_builder = JSONOutput()

        while True:
            result_dict = servertrak.execute_command(proxy, servers, users, 
                                                     command, False, output_builder)
            results = {}
            for result in result_dict:
                success = int(result['success'])
                if success == 0:
                    users = 0
                    cpu_load = 0
                else:
                    uptime_str = result['output']
                    uptime, users, load = uptime_str.split(',')
                    users = users.lstrip().split(' ')[0]
                    cpu_load = load.lstrip().split(':')[1].lstrip()

                self.dbproxy.add_stat(result['hostname'], {
                    'host': result['hostname'],
                    'date': datetime.now().isoformat(),
                    'users': users,
                    'cpu_load': cpu_load
                })

            time.sleep(60 * 5)
