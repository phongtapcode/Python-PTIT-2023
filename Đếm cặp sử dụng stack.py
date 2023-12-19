n = int(input())
ans = 0
stack = []
cnt = {}

for i in range(1, n + 1):
    x = int(input())
    while stack and x > stack[-1]:
        cnt[stack[-1]] -= 1
        stack.pop()
        ans += 1
    if stack:
        if x == stack[-1]:
            ans += cnt[x] + (len(stack) > cnt[x])
        else:
            ans += 1
    stack.append(x)
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

print(ans)