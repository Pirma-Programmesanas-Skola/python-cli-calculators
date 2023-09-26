def main():
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }

    ops_list = list(ops.keys())

    op = input(f"Ievadiet darbību ({', '.join(ops_list)}): ")
    if op not in ops_list:
        exit_with_msg("Nepareiza darbība")

    sk1 = input_number("Ievadiet 1. skaitli: ")
    sk2 = input_number("Ievadiet 2. skaitli: ")

    res = ops[op](sk1, sk2)
    print(f"Rezultāts: {sk1} {op} {sk2} =", res)


def is_float(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


def exit_with_msg(msg):
    print(msg)
    exit()


def input_number(prompt):
    x = input(prompt)
    if not is_float(x):
        exit_with_msg("Nepareizs skaitlis.")
    return float(x)


main()
