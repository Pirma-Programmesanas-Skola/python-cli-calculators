op = input("Ievadiet darbību (+,-,*,/): ")
sk1 = int(input("Ievadiet 1. skaitli: "))
sk2 = int(input("Ievadiet 2. skaitli: "))

if op == '+':
    rez = sk1 + sk2
elif op == '-':
    rez = sk1 - sk2
elif op == '*':
    rez = sk1 * sk2
elif op == '/':
    rez = sk1 / sk2
else:
    print("Nepareiza darbība.")
    exit()

print("Rezultāts: " + str(rez))
