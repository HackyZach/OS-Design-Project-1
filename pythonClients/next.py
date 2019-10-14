import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000") as proxy:
    print("Waiting on tuples...")

    res = proxy._rd_a([{ 'class': 'String'}, "distsys", { 'class': 'String' } ])

    print("Sent tuples...")

    print(res)
    
    print("Tuples received...")
