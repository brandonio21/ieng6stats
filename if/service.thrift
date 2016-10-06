struct Server {
  1: string hostname;
}

struct ServerStat {
  1: Server hostname;
  2: string date;
  3: i32 users;
  4: i32 cpu_load;
}

struct ServerStatCollection {
  1: Server hostname;
  2: list<ServerStat> stats;
}

service ServerStatService {
  
  list<ServerStatCollection> getAllServerStats();

  list<ServerStat> getAllCurrentStats();

  ServerStat getCurrentStat(1: string hostname);

  ServerStatCollection getCurrentStats(1: string hostname);

}
