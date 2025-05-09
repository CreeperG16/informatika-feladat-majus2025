print("- 1. feladat")
n = 1
while n <= 10:
    if n % 2 == 0: print(n)
    n += 1

print("\n- 2. feladat")
n = 10
while n > 0:
    print(n)
    n -= 1

print("\n- 3. feladat")
n = 10
while n > 0:
    if n % 2 == 1: print(n)
    n -= 1

print("\n- 4. feladat")
text = input("Mi legyen a szöveg? ")
n = int(input("Hányszor írja ki a szöveget? "))
while n > 0:
    print(text)
    n -= 1

print("\n- 5. feladat")
n = 1
while n % 2 == 1:
    n = int(input("Egy páros szám: "))

print("\n- 6. feladat")
from random import randint as ri
n = 20
numThree = 0
while n > 0:
    x = ri(1, 12)
    n -= 1
    if x % 3 != 0: continue

    print(x)
    numThree += 1
print(f"Összesen {numThree} darab hárommal osztható szám lett generálva.")
