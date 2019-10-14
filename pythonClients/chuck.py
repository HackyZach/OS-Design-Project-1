import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000") as proxy:
    print("Waiting on tuples...")

    res = proxy._rd(["bob", "distsys", { 'class': 'String' } ])
    res2 = proxy._rd(["alice" , "gtcn", { 'class': 'String'} ])
    res3 = proxy._rd(["bob" , "gtcn", { 'class': 'String'} ])

    print("Sent tuples...")

    print(res)
    print(res2)
    print(res3)

    print("Tuples received...")
