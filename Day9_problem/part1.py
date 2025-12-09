points = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(","))
        points.append((x, y))

max_area = 0

for i in range(len(points)):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]

        if x1 != x2 and y1 != y2:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            max_area = max(max_area, area)

print(max_area)

