from servertrak.servertraker import ServerTraker
from servertrak.common.server import Server
from servertrak.common.user import User
from servertrak.proxies.ssh import SSHProxy
from servertrak.format.jsonoutput import JSONOutput

import json
import time
from datetime import datetime

class ServerStatDaemon(object):
    def __init__(self, 
                 dbproxy, 
                 host_discovery_modules, 
                 output_builder, 
                 servertrak_proxy):
        self.servertraker = ServerTraker(
            host_discovery_modules, output_builder, servertrak_proxy
        )
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
            result_dict = json.loads(result_dict)
            results = {}
            for result in result_dict:
                success = int(result['success'])
                if success == 0:
                    users = 0
                    cpu_load = 0
                else:
                    uptime_str = result['output']
                    uptime, _, users, load, _, _ = uptime_str.split(',')
                    users = users.lstrip().split(' ')[0]
                    cpu_load = load.lstrip().split(':')[1].lstrip()

                self.dbproxy.add_stat(result['server'], {
                    'host': result['server'],
                    'date': datetime.now().isoformat(),
                    'users': users,
                    'cpu_load': cpu_load
                })

            time.sleep(60 * 5)
