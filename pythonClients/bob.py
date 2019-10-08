import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000")

print("Proxy made...")

tuples = [
  ["bob","distsys","I am studying chapter 2"],
  ["bob","distsys","The rinda exmaple's not that simple"]
]

print("Tuples Ready...")

proxy._out(tuples[0])
proxy._out(tuples[1])

print("Tuples Sent...")
