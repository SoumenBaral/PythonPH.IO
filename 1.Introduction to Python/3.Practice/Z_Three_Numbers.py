k, s = input().split()
k = int(k)
s = int(s)
counter = 0
for i in range(k+1):
    for j in range(k+1):
        if s - i - j >= 0 and s - i - j <= k:
            counter += 1

print(counter)