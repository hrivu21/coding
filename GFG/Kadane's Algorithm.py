def kadane(l):
    currsum = l[0]
    maxsum = l[0]
    for i in range(1, len(l)):
        if currsum + l[i] < l[i]:
            currsum = l[i]
        else:
            currsum += l[i]
        maxsum = max(maxsum, currsum)
    return maxsum


t = int(input())
for _ in range(t):
    input()
    l = list(map(int, input().split()))
    print(kadane(l))
