import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000", allow_none=True) as proxy:
    print("Proxy made...")

    tuples = [
      ["alice","gtcn","This graph theory stuff is not easy"],
      ["alice","distsys","I like systems more than graphs"]
    ]

    print("Tuples Ready...")

    proxy._out(tuples[0])
    proxy._out(tuples[1])

    print("Tuples Sent...")
