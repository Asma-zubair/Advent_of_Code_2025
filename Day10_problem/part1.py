import re
import itertools
def gaussian_elimination(A, b):
    A = [row[:] for row in A]
    b = b[:]
    n = len(A)       
    m = len(A[0])    
    pivot_col = [-1] * n
    row = 0
    for col in range(m):
        pivot = None
        for r in range(row, n):
            if A[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        b[row], b[pivot] = b[pivot], b[row]
        pivot_col[row] = col
        for r in range(n):
            if r != row and A[r][col] == 1:
                for c in range(col, m):
                    A[r][c] ^= A[row][c]
                b[r] ^= b[row]
        row += 1
        if row == n:
            break
    for r in range(n):
        if pivot_col[r] == -1 and b[r] == 1:
            return None
    x0 = [0] * m
    for r in range(n - 1, -1, -1):
        if pivot_col[r] == -1:
            continue
        col = pivot_col[r]
        s = b[r]
        for c in range(col + 1, m):
            s ^= (A[r][c] & x0[c])
        x0[col] = s
    free_vars = [c for c in range(m) if c not in pivot_col]
    basis = []
    for fv in free_vars:
        vec = [0] * m
        vec[fv] = 1
        for r in range(n):
            pc = pivot_col[r]
            if pc != -1 and A[r][fv] == 1:
                vec[pc] ^= 1
        basis.append(vec)
    return x0, basis
def solve_machine(pattern, buttons):
    target = [1 if c == '#' else 0 for c in pattern]
    n = len(target)
    m = len(buttons)
    A = [[0] * m for _ in range(n)]
    for j, toggles in enumerate(buttons):
        for t in toggles:
            A[t][j] = 1
    res = gaussian_elimination(A, target)
    if res is None:
        return float("inf")
    x0, basis = res
    best = sum(x0)
    for mask in range(1 << len(basis)):
        x = x0[:]
        for i in range(len(basis)):
            if (mask >> i) & 1:
                x = [ (x[k] ^ basis[i][k]) for k in range(m) ]
        best = min(best, sum(x))
    return best
def parse_input(lines):
    results = []
    for line in lines:
        line = line.strip()
        pattern = re.search(r"\[(.*?)\]", line).group(1)
        buttons = []
        for part in re.findall(r"\((.*?)\)", line):
            if part.strip() == "":
                buttons.append([])
            else:
                nums = list(map(int, part.split(",")))
                buttons.append(nums)
        results.append((pattern, buttons))
    return results
def main():
    with open("input.txt") as f:
        lines = f.readlines()
    machines = parse_input(lines)
    total = 0
    for pattern, buttons in machines:
        total += solve_machine(pattern, buttons)
    print(total)
if __name__ == "__main__":
    main()