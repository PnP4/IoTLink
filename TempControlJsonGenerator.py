"a|b|c"
import json

data={}
data["seq"]=[{"seqno":1,"name":"a"},{"seqno":2,"name":"b"},{"seqno":3,"name":"c"},{"seqno":4,"name":"d"}]
data["you"]="a"
data["a"]=[{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0}]
data["b"]=[{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0}]
data["c"]=[{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0}]
data["d"]=[{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0},{"ip":"127.0.0.1","port":8080,"avialable":0}]

print json.dumps(data)