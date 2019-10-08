import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000/RPC2")

res = proxy._in(["bob",str,str])
res2 = proxy._in([str,"distsys",str])

print(res)
print(res2)
