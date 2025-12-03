
with open("input.txt", "r") as f:
    banks = [line.strip() for line in f.readlines() if line.strip()]

total = 0

for bank in banks:
    best = 0
    n = len(bank)

    # Check all pairs i < j
    for i in range(n):
        a = int(bank[i])
        for j in range(i + 1, n):
            b = int(bank[j])
            val = 10 * a + b
            if val > best:
                best = val

    total += best

print("Total Output Joltage:", total)
