import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000") as proxy:
    print("Proxy made...")

    tuples = [
      ["alice","distsys","This graph theory stuff is not easy"],
      ["alice","distsys","I like systems more than graphs"]
    ]

    print("Tuples Ready...")

    proxy._out(tuples[0])
    proxy._out(tuples[1])

    print("Tuples Sent...")
