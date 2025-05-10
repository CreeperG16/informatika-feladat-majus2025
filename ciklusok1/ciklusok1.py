print("- 1. feladat")
n = 1
while n <= 10:
    print(n)
    n += 1

print("\n- 2. feladat")
szamlalo = 1
while szamlalo <= 5:
    print("Programozni jó!")
    szamlalo += 1

print("\n- 3. feladat")
cont = True
while cont:
    print("Vidd ki a szemetet!")
    cont = input("Mondjam még egyszer? (i/n) ") != "n"
print("Program vége!")
