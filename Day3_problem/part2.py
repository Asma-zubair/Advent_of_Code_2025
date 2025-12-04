

with open("input2.txt", "r") as f:
    banks = [line.strip() for line in f.readlines() if line.strip()]

total = 0

for bank in banks:
    k = 12                  
    result = []             
    start = 0
    n = len(bank)

   
    for _ in range(k):
       
        end = n - (k - len(result)) + 1

        
        best_digit = '0'
        best_index = start

        for i in range(start, end):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_index = i

        result.append(best_digit)
        start = best_index + 1

    
    total += int("".join(result))

print("Total Output Joltage:", total)
