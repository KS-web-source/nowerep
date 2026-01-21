print("Aby korzystać z kalkulatora należy najpierw podać dwie liczby, A oraz B, a następnie znak operacji, jaką chcemy wykonać (+, -, *, /, **")
a = float(input("Podaj A: "))
b = float(input("Podaj B: "))
operacja = input("Podaj operacje: ")
if operacja == "+":
    print(f'{a} + {b} = {a + b}')
elif operacja == "-":
    print(f"{a} - {b} = {a - b}")
elif operacja == '*':
    print ( f'{a} * {b} = {a*b}')

elif operacja =="/":
    if b == 0:
        print("Błąd, dzielenie przez zero")
        break
    print(f"{a} / {b} = {a / b}")
    if b==0:
    print(*Blad, dzielenie przez zero*)
    break
elif operacja =="**":
    print(f"{a} ** {b} = {a ** b}")