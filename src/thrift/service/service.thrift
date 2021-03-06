struct Server {
  1: string hostname;
}

struct ServerStat {
  1: Server host;
  2: string date;
  3: i32 users;
  4: i32 cpu_load;
}

struct ServerStatCollection {
  1: Server host;
  2: list<ServerStat> stats;
}

service ServerStatService {
  ServerStat getLatestStat(1: Server host);
  string ping();
}
