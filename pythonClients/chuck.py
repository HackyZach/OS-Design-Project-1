import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000", allow_none=True)

#res = proxy._in(["bob", { 'class': 'String' }, { 'class': 'String' }])
#res2 = proxy._in([{ 'class': 'String' }, "distsys", { 'class': 'String' }])

print("Waiting on tuples...")

res = proxy._in(["bob", None, None])
res2 = proxy._in([None, "distsys", None])

print(res)
print(res2)

print("Tuples received...")