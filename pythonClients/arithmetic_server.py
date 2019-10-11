import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:5000", allow_none=True)

print("Waiting on tuples...")

arguments = [
    proxy._in([None, None, None]),
    proxy._in([None, None, None]),
    proxy._in([None, None, None]),
    proxy._in([None, None, None]),
    proxy._in([None, None, None]),
]

result = []
lhs = 0
rhs = 0
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

    result.append(lhs + " = " + rhs)

for complete_equation in result:
    print(complete_equation)

print("Tuples received...")