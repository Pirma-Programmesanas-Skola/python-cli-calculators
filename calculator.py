print("Hello, welcome to the calculator program!")
print("The calculator evaluates expressions in the form:")
print("<number> <operator> <number> ... <operator> <number>")
print("This calculator also supports parentheses")
print("for example: (2+2)*2+1 + 2 * 31 - 4 / 2^2^3")


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

    expression = input('Enter an expression: ')

    ops_symbols = [op['op'] for op in ops]
    parsed = parse(expression, ops_symbols)  # [2,'+',2,'*',2]

    print(parsed)
    evaluate(parsed, ops)
    print(parsed)


def evaluate(parsed_exp, ops):
    print("parsed_exp: ", parsed_exp)

    while '(' in parsed_exp:
        if ')' not in parsed_exp:
            print("Invalid: missing ')'")
            exit()
        fst_open = parsed_exp.index('(')
        lst_open = len(parsed_exp) - parsed_exp[::-1].index(')') - 1
        i, j = fst_open, lst_open
        sub_exp = parsed_exp[i + 1:j]
        evaluate(sub_exp, ops)
        print("sub_exp: ", sub_exp)
        parsed_exp[i] = sub_exp[0]
        parsed_exp.pop(i + 1)
        parsed_exp.pop(i + 1)

    min_p = min([op['p'] for op in ops])
    max_p = max([op['p'] for op in ops])

    parsed_exp = []
    for p in range(min_p, max_p + 1):
        p_ops = [op for op in ops if op['p'] == p]
        p_ops_symbols = [op['op'] for op in p_ops]
        for i in range(len(parsed_exp)):
            x = parsed_exp[i]
            if x in p_ops_symbols:
                op = [op for op in p_ops if op['op'] == x][0]
                f_val = op['f'](parsed_exp[i - 1], parsed_exp[i + 1])
                if op['ltr']:
                    parsed_exp[i - 1] = f_val
                else:
                    parsed_exp[i + 1] = f_val
                parsed_exp.pop(i)
                parsed_exp.pop(i)
                print(parsed_exp)

    print("result: ", parsed_exp)


def parse(expression, ops_symbols):
    """Parses an expression into a list of numbers and operators"""
    expression = expression.replace(" ", "").strip().replace("\t", "").lower()
    res = []

    def is_sep(c):
        return c in ops_symbols or c in ['(', ')']

    # seperate digits from symbols
    for i in range(len(expression)):
        if i == 0:
            res.append(expression[i])
        else:
            if is_sep(expression[i]):
                res.append(expression[i])
            else:
                if is_sep(expression[i - 1]):
                    res.append(expression[i])
                else:
                    res[-1] += expression[i]

    for i in range(len(res)):
        try:
            res[i] = float(res[i])
        except ValueError:
            if res[i] in ops_symbols:
                continue
            if res[i] in ['(', ')']:
                continue
            print(f"Invalid: \"{res[i]}\"")
            exit()
    return res


if __name__ == '__main__':
    main()
