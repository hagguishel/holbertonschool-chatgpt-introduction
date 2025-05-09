#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <non-negative-integer>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError("Le nombre doit être non-négatif.")
except ValueError as e:
    print("Erreur:", e)
    sys.exit(1)

f = factorial(num)
print(f)
