

from bisect import bisect_left, bisect_right

INPUT = "input2.txt"

def read_points(path):
    pts = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x,y = line.split(",")
            pts.append((int(x), int(y)))
    return pts

def build_edges(pts):
    edges = []
    n = len(pts)
    for i in range(n):
        x1,y1 = pts[i]
        x2,y2 = pts[(i+1)%n]
        edges.append((x1,y1,x2,y2))
    return edges

def intervals_at_y(edges, y):
    inter_x = []
    horizontals = []

    for (x1,y1,x2,y2) in edges:
        if y1 == y2:
            if y == y1:
                horizontals.append((min(x1,x2), max(x1,x2)))
        else:
            ymin = min(y1,y2)
            ymax = max(y1,y2)
            if ymin <= y < ymax:
                inter_x.append(x1)

    inter_x.sort()
    intervals = []

    for i in range(0, len(inter_x), 2):
        if i+1 < len(inter_x):
            a = inter_x[i]
            b = inter_x[i+1]
            intervals.append((a,b))

    intervals.extend(horizontals)
    if not intervals:
        return []

    intervals.sort()
    merged = []
    cur_a, cur_b = intervals[0]
    for a,b in intervals[1:]:
        if a <= cur_b + 1:
            cur_b = max(cur_b, b)
        else:
            merged.append((cur_a, cur_b))
            cur_a, cur_b = a, b
    merged.append((cur_a, cur_b))
    return merged

def rectangle_inside(x0, x1, y0, y1, sample_ys, intervals_map):
    lo = bisect_left(sample_ys, y0)
    hi = bisect_right(sample_ys, y1)
    if lo >= hi:
        return False

    for idx in range(lo, hi):
        sy = sample_ys[idx]
        ivs = intervals_map[sy]

        k = bisect_right(ivs, (x0, 10**18)) - 1
        ok = False
        if k >= 0:
            a,b = ivs[k]
            if a <= x0 and b >= x1:
                ok = True
        if not ok:
            return False

    return True

def compute_part2(red_pts):
    edges = build_edges(red_pts)

    ys = [p[1] for p in red_pts]
    unique_y = sorted(set(ys))
    sample_ys = set(unique_y)

    for i in range(len(unique_y)-1):
        a = unique_y[i]
        b = unique_y[i+1]
        if a+1 <= b-1:
            sample_ys.add(a+1)

    sample_ys = sorted(sample_ys)

    intervals_map = {}
    for sy in sample_ys:
        intervals_map[sy] = intervals_at_y(edges, sy)

    n = len(red_pts)
    max_area = 0

    for i in range(n):
        x1,y1 = red_pts[i]
        for j in range(i+1, n):
            x2,y2 = red_pts[j]

            if x1 == x2 or y1 == y2:
                continue

            xl = min(x1,x2)
            xr = max(x1,x2)
            yb = min(y1,y2)
            yt = max(y1,y2)

            area = (xr - xl + 1) * (yt - yb + 1)
            if area <= max_area:
                continue

            if rectangle_inside(xl, xr, yb, yt, sample_ys, intervals_map):
                max_area = area

    return max_area

if __name__ == "__main__":
    pts = read_points(INPUT)
    print(compute_part2(pts))
