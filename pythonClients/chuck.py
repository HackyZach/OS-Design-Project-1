import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000")

#res = proxy._in(["bob", { 'class': 'String' }, { 'class': 'String' }])
#res2 = proxy._in([{ 'class': 'String' }, "distsys", { 'class': 'String' }])

print("Waiting on tuples...")

res = proxy._in(["bob", { 'class': 'String' }, { 'class': 'String' }])
res2 = proxy._in([{ 'class': 'String'} , "distsys", { 'class': 'String'} ])
res3 = proxy._in([{ 'class': 'String'} , "distsys", { 'class': 'Numeric'} ])
res4 = proxy._in([{ 'class': 'String'} , "distsys", { 'class': 'String'} ])

print("Sent tuples...")

print(res)
print(res2)
print(res3)
print(res4)

print("Tuples received...")
