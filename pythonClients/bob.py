import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000", allow_none=True) as proxy:
    print("Proxy made...")

    tuples = [
      ["bob","distsys","I am studying chapter 2"],
      ["bob","distsys","The rinda exmaple's not that simple"],
      ["bob","distsys",1234],
      ["bob","distsys",678],
      ["bob","distsys",4784],
      ["bob","distsys","ehhh...."]
    ]

    print("Tuples Ready...")

    proxy._out(tuples[0])
    proxy._out(tuples[1])
    proxy._out(tuples[2])
    proxy._out(tuples[3])
    proxy._out(tuples[4])
    proxy._out(tuples[5])

    print("Tuples Sent...")
