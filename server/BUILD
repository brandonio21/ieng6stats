python_binary (
  name="server",
  source = "server.py",
  dependencies = [
    ":ieng6handler",
    ":ieng6daemon",
    "//server/3rdparty:thrift",
    "//service:ieng6service",
    "//server/proxies:dbproxy-lib",
  ],
)

python_binary (
  name="remote",
  source="remote.py",
  dependencies = [
    "//server/3rdparty:thrift",
    "//service:ieng6service",
  ],
)

python_library (
  name="ieng6handler",
  sources = [
    "handler.py",
  ],
  dependencies = [
    "//service:ieng6service",
    "//server/proxies:dbproxy-lib",
  ],
)

python_library (
  name="ieng6daemon",
  sources = [
    "daemon.py",
  ],
  dependencies = [
    "//server/servertrak:servertrak",
    "//server/proxies:dbproxy-lib",
  ],
)
