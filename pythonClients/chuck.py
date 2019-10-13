import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000", allow_none=True)

#res = proxy._in(["bob", { 'class': 'String' }, { 'class': 'String' }])
#res2 = proxy._in([{ 'class': 'String' }, "distsys", { 'class': 'String' }])

print("Waiting on tuples...")

res = proxy._in(["bob", { 'class': 'String' }, { 'class': 'String' }])
#res2 = proxy._in([str, "distsys", str])
#res3 = proxy._in([str, "distsys", None])

print(res)
print(res2)

print("Tuples received...")
