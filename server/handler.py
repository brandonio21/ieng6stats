from .ieng6service.types import Server, ServerStat

class ServerStatServiceHandler(object):
    def __init__(self, dbproxy):
        self.dbproxy = dbproxy

    def getLatestStat(self, server):
        stat_dict = self.dbproxy.get_latest_stat(server.hostname)
        return self._dict_to_stat(stat_dict)

    def _dict_to_stat(self, stat_dict):
        stat = ServerStat()
        stat.host = Server(stat_dict['hostname'])
        stat.date = stat_dict['date']
        stat.users = stat_dict['users']
        stat.cpu_load = stat_dict['cpu_load']

        return stat
