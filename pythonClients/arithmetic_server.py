import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000")

lhs = 0
rhs = 0
condition = True
while condition:
    print("Waiting on tuples...")
    arguments = [proxy._in([{'class': 'String'}, {'class': 'Numeric'}, {'class': 'Numeric'}])]

    for equation in arguments:
        rhs = str(equation[1]) + ' ' + str(equation[0]) + ' ' + str(equation[2])

        if equation[0] == '*':
            lhs = str(equation[1] * equation[2])
        elif equation[0] == '+':
            lhs = str(equation[1] + equation[2])
        elif equation[0] == '-':
            lhs = str(equation[1] - equation[2])
        elif equation[0] == '%':
            lhs = str(equation[1] % equation[2])
        elif equation[0] == '^':
            lhs = str(equation[1] ^ equation[2])
        else:
            lhs = "Invalid operator"

    proxy._out([(lhs + " = " + rhs),"eqRes"])

    print("Tuples computed and sent back...")
