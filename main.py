import math

a = int(input("Input A: "))
b = int(input("Input B: "))
c = int(input("Input C: "))

disc = b**2 - 4*a*c

if disc >= 0:
    root = math.sqrt(disc)
    ans1 = (-b + root) / (2 * a)
    ans2 = (-b - root) / (2 * a)
    print(f"Solutions: {ans1}, {ans2}")
else:
    print("No real solutions (disc is negative)")