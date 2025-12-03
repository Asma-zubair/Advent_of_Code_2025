# Read all banks from input.txt
with open("input2.txt", "r") as f:
    banks = [line.strip() for line in f.readlines() if line.strip()]

total = 0

for bank in banks:
    k = 12                  # number of digits to pick
    result = []             # chosen digits
    start = 0
    n = len(bank)

    # Greedy: each time choose the largest digit available
    for _ in range(k):
        # Range where next digit can be selected
        end = n - (k - len(result)) + 1

        # Find max digit in range [start, end)
        best_digit = '0'
        best_index = start

        for i in range(start, end):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_index = i

        result.append(best_digit)
        start = best_index + 1

    # Convert selected digits to number
    total += int("".join(result))

print("Total Output Joltage:", total)
