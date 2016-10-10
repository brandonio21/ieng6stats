ieng6stats
==========
A tool, in progress, which will allow the creation of a dashboard which reports statistics for
several hosts. 

Building
--------
[pantsbuild](https://github.com/pantsbuild/pants) is used to build the server, which can be 
done with:

```
./pants binary //server:server
```

This will build `dist/server.pex` which will be used to receive and process requests for
statistics and will also manage a daemon, which occasionally retrieves new statistics for
the host.


Daemon/Handler Exclusivity
--------------------------
By design, the daemon (which retrieves host information) and request handler are independent
of eachother. This is to ensure that DDoS-style requests do not impact the hosts that are
being tracked.
