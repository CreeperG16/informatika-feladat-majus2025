print("- 1. feladat")
for n in range(1, 11):
    if n % 2 == 0: print(n)

print(", ".join([str(n) for n in range(2, 11, 2)]))

print("\n- 2. feladat")
for n in range(10, 0, -1):
    print(n)

print(", ".join([str(n) for n in range(10, 0, -1)]))

print("\n- 3. feladat")
for n in range(9, 0, -2):
    print(n)

print(", ".join([str(n) for n in range(9, 0, -2)]))

print("\n- 4. feladat")
text = input("Mi legyen a szöveg? ")
n = int(input("Hányszor írja ki a szöveget? "))
for _ in range(n):
    print(text)

print("\n- 5. feladat")
while int(input("Egy páros szám: ")) % 2 == 1: pass

print("\n- 6. feladat")
from random import randint as ri
nums = [ri(1, 12) for _ in range(20)]
three = list(filter(lambda x: x % 3 == 0, nums))
print(", ".join([str(x) for x in three]))
print(f"Összesen {len(three)} darab hárommal osztható szám lett generálva.")
