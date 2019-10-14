import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000") as proxy:
    print("Proxy made...")

    tuples = [
      ["bob","distsys","I am studying chapter 2"],
      ["bob","distsys","The rinda exmaple's not that simple"],
      ["bob","distsys","ehhh...."],
      ["bob","distsys","It's only a distributed systems model..."],
    ]

    print("Tuples Ready...")

    proxy._out(tuples[0])
    proxy._out(tuples[1])
    proxy._out(tuples[2])
    proxy._out(tuples[3])

    print("Tuples Sent...")
