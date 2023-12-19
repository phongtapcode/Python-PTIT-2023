from collections import deque

# Hàm tính số bước tối thiểu
def min_steps(n, m, a):
    d = [[-1 for _ in range(m)] for _ in range(n)]
    dx = [1, 0, 1]
    dy = [0, 1, 1]

    # BFS từ ô (0, 0)
    q = deque()
    q.append((0, 0))
    d[0][0] = 0

    # Loang từ đầu hàng đợi
    check = 0
    while q:
        i, j = q.popleft()
        for k in range(3):
            if k == 0 and j + 1 < m:
                step = abs(a[i][j] - a[i][j + 1])
                i1, j1 = i, j + step
            elif k == 1 and i + 1 < n:
                step = abs(a[i][j] - a[i + 1][j])
                i1, j1 = i + step, j
            elif k == 2 and i + 1 < n and j + 1 < m:
                step = abs(a[i][j] - a[i + 1][j + 1])
                i1, j1 = i + step, j + step

            if 0 <= i1 < n and 0 <= j1 < m and d[i1][j1] == -1:
                q.append((i1, j1))
                d[i1][j1] = d[i][j] + 1

    if d[n-1][m-1] == -1:
        return -1
    return d[n-1][m-1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    result = min_steps(n, m, a)
    print(result)