import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000") as proxy:
    print("Proxy made...")

    tuples = [
      ["*", 2, 2],
      ["+", 2, 5],
      ["-", 9, 3],
      ["%", 9145, 67],
      ["^", 10, 4],
    ]

    tupleResAbstract = [None,"eqRes"]
    print("Tuples Ready...")

    proxy._out(tuples[0])
    proxy._out(tuples[1])
    proxy._out(tuples[2])
    proxy._out(tuples[3])
    proxy._out(tuples[4])

    print("Tuples Sent...")

    print(proxy._in(tupleResAbstract)[0])
    print(proxy._in(tupleResAbstract)[0])
    print(proxy._in(tupleResAbstract)[0])
    print(proxy._in(tupleResAbstract)[0])
    print(proxy._in(tupleResAbstract)[0])
