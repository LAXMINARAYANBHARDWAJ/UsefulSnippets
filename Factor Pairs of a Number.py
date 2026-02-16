def factor_pairs(n):
    pairs = []
    for i in range(1, int(n**0.5) + 1, 1):
        if n % i == 0:
            pairs.append((i, n // i))
    return pairs

num = int(input("Number>>> "))
factors = factor_pairs(num)

output = " | ".join(f"({a}, {b})" for a, b in factors)
print(output)
