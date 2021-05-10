# function should return True/False
def interleaved(a, b, c, i1, i2, i3):
    if i1 == len(a):
        return b[i2:] == c[i3:]
    if i2 == len(b):
        return a[i1:] == c[i3:]

    if a[i1] == c[i3] and b[i2] == c[i3]:
        return interleaved(a, b, c, i1+1, i2, i3+1) or interleaved(a, b, c, i1, i2+1, i3+1)
    elif a[i1] == c[i3]:
        return interleaved(a, b, c, i1+1, i2, i3+1)
    elif b[i2] == c[i3]:
        return interleaved(a, b, c, i1, i2+1, i3+1)
    else:
        return False


def isInterleave(A, B, C):
    # Code here
    if len(A) + len(B) != len(C):
        return False
    return interleaved(A, B, C, 0, 0, 0)


# {
#  Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        if isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)
# contributed By: Harshit Sidhwa
# } Driver Code Ends
