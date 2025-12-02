

puzzle_input = "10327-17387,74025-113072,79725385-79874177,964628-1052240,148-297,3-16,126979-227778,1601-2998,784-1207,831289-917268,55603410-55624466,317-692,602197-750430,17-32,38-58,362012-455626,3622441-3647505,883848601-883920224,62-105,766880-804855,9184965756-9185005415,490073-570277,2929273115-2929318135,23251-48475,9696863768-9697013088,229453-357173,29283366-29304416,4526-8370,3095-4389,4400617-4493438"  



def is_invalid_part2(number):
    s = str(number)
    n = len(s)
    
    
    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue 
        
        block = s[:size]
        repeats = n // size
        
        
        if block * repeats == s and repeats >= 2:
            return True
    
    return False



total_sum = 0

ranges = puzzle_input.split(",")

for part in ranges:
    if "-" not in part:
        continue
    start, end = part.split("-")
    start = int(start)
    end = int(end)
    
    
    for num in range(start, end + 1):
        if is_invalid_part2(num):
            total_sum += num


print("Total sum of invalid IDs (Part 2):", total_sum)
