import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000", allow_none=True) as proxy:
    print("Proxy made...")

    tuples = [
      ["bob","distsys","I am studying chapter 2"],
      ["bob","distsys","The rinda exmaple's not that simple"]
      ["bob","distsys",1234]
      ["bob","None",6675866]
    ]

    print("Tuples Ready...")

    proxy._out(tuples[0])
    proxy._out(tuples[1])
    proxy._out(tuples[2])
    proxy._out(tuples[3])

    print("Tuples Sent...")
