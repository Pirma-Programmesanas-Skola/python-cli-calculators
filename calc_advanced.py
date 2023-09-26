print("Hello, welcome to the calculator program!")
print("The calculator evaluates expressions in the form:")
print("<number> <operator> <number> ... <operator> <number>")
print("for example: 1 + 2 * 31 - 4 / 2^2^3")


def main():
    ops = [
        {'op': '^', 'ltr': False,
         'f': lambda x, y: x ** y, 'p': 1},

        {'op': '*', 'ltr': True,
         'f': lambda x, y: x * y, 'p': 2},

        {'op': '/', 'ltr': True,
         'f': lambda x, y: x / y, 'p': 2},

        {'op': '+', 'ltr': True,
         'f': lambda x, y: x + y, 'p': 3},

        {'op': '-', 'ltr': True,
         'f': lambda x, y: x - y, 'p': 3}
    ]

    ops_symbols = [op['op'] for op in ops]

    expression = input('Enter an expression: ')
    parsed = parse(expression, ops_symbols)  # [2,'+',2,'*',2]

    print(parsed)

    min_p = min([op['p'] for op in ops])
    max_p = max([op['p'] for op in ops])

    for p in range(min_p, max_p + 1):
        p_ops = [op for op in ops if op['p'] == p]
        p_ops_symbols = [op['op'] for op in p_ops]
        for x in parsed:
            if x in p_ops_symbols:
                op = [op for op in p_ops if op['op'] == x][0]
                i = parsed.index(x)
                if op['ltr']:
                    parsed[i - 1] = op['f'](parsed[i - 1], parsed[i + 1])
                else:
                    parsed[i + 1] = op['f'](parsed[i - 1], parsed[i + 1])
                parsed.pop(i)
                parsed.pop(i)
                print(parsed)


def parse(expression, ops_symbols):
    """Parses an expression into a list of numbers and operators"""
    expression = expression.replace(" ", "").strip().replace("\t", "").lower()
    res = []
    # seperate digits from symbols
    for i in range(len(expression)):
        if i == 0:
            res.append(expression[i])
        else:
            if expression[i] in ops_symbols:
                res.append(expression[i])
            else:
                if expression[i - 1] in ops_symbols:
                    res.append(expression[i])
                else:
                    res[-1] += expression[i]

    for i in range(len(res)):
        try:
            res[i] = float(res[i])
        except ValueError:
            if res[i] not in ops_symbols:
                print("Invalid operator: " + res[i])
                exit()
            pass
    return res


if __name__ == '__main__':
    main()
