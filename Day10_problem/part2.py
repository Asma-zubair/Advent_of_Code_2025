import re
from pulp import (
    LpProblem, LpMinimize, LpVariable,
    LpInteger, lpSum, LpStatusOptimal
)
def parse_line(line):
    buttons = [tuple(map(int, g.split(',')))
               for g in re.findall(r"\(([\d,]+)\)", line)]
    target = list(map(int, re.findall(r"\{([\d,]+)\}", line)[0].split(',')))
    return buttons, target
def solve_machine(buttons, target):
    m = len(target)
    n = len(buttons)
    prob = LpProblem("MachinePressMin", LpMinimize)
    x = [LpVariable(f"x_{i}", lowBound=0, cat=LpInteger) for i in range(n)]
    prob += lpSum(x)
    for c in range(m):
        prob += lpSum(x[i] for i in range(n) if c in buttons[i]) == target[c]
    status = prob.solve()
    if status != LpStatusOptimal:
        raise RuntimeError("No optimal solution found")
    return sum(int(v.value()) for v in x)
def main():
    total = 0
    with open("input2.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            buttons, target = parse_line(line)
            presses = solve_machine(buttons, target)
            total += presses
    print("Final Answer:", total)
if __name__ == "__main__":
    main()