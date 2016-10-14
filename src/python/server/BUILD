python_binary (
  name="server",
  source = "server.py",
  dependencies = [
    ":ieng6handler",
    ":ieng6daemon",
    "//3rdparty/python:thrift",
    "//src/thrift/service:ieng6service",
    "//src/python/server/proxies:dbproxy-lib",
  ],
)

python_binary (
  name="remote",
  source="remote.py",
  dependencies = [
    "//3rdparty/python:thrift",
    "//src/thrift/service:ieng6service",
  ],
)

python_library (
  name="ieng6handler",
  sources = [
    "handler.py",
  ],
  dependencies = [
    "//src/thrift/service:ieng6service",
    "//src/python/server/proxies:dbproxy-lib",
  ],
)

python_library (
  name="ieng6daemon",
  sources = [
    "daemon.py",
  ],
  dependencies = [
    "//src/python/server/servertrak:servertraklib",
    "//src/python/server/servertrak/proxies",
    "//src/python/server/servertrak/common",
    "//src/python/server/servertrak/format",
    "//src/python/server/proxies:dbproxy-lib",
  ],
)
