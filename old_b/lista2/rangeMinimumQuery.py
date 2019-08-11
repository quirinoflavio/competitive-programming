from math import log
MAXN = 100000
K = 16

def fillsST(arr, n):
    for i in range(n):
        st[i][0] = arr[i]
    
    j = 1
    while (1 << j) <= n:
        i = 0
        while (i + (1 << j) -1) < n:
            if (st[i][j-1] < st[i + (1<<(j-1))][j-1]):
                st[i][j] = st[i][j-1]
            else:
                st[i][j] = st[i + (1 << (j-1))][j-1]
            i += 1
        j += 1

def query(L, R):
    j = int(log(R - L + 1, 2))
    if st[L][j] <= st[R - (1 << j) + 1][j]:
        return st[L][j]
    else:
        return st[R - (1<<j) + 1][j]


n = int(input())
#a = [5,3,8,5,5,6,5,4,7,8,9,6,5,4,7,8,9,6,5,4,2,8,9,6,5,4,7,8,9,6,5,4,7,8,9,6,5,4,7,8,9,6,1]
array = list(map(int, input().split()))
k = int(log(n, 2)) + 1
st = [[0 for i in range(k)] for x in range(n)]
fillsST(array, n)

q = int(input())
for i in range(q):
    l, r = list(map(int, input().split()))
    print(query(l, r))
