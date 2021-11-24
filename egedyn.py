import random
B = []
N = int(input())
A = []
j = 0
k = 0
kstore = 0
for i in range (N):
    A.append([0]*N)
    B.append([0]*N)
print(A)
print(B)
for i in range (N):
    for h in range (N):
        B[i][h] = random.randint(1,10)
print (B)
while True:
    print (j,k)
    if B[j][k] % 3 == 0:
        if j == k == 0:
            A[j][k] = B[j][k]
        elif j == 0:
            A[j][k] = A[j - 1][k] + B[j][k]
        elif k == 0:
            A[j][k] = A[j][k - 1] + B[j][k]
        else:
            A[j][k] = max(A[j - 1][k],A[j][k - 1]) + B[j][k]
    else:
        if j == k == 0:
            A[j][k] = 0
        elif j == 0:
            A[j][k] = A[j - 1][k]
        elif k == 0:
            A[j][k] = A[j][k - 1]
        else:
            A[j][k] = max(A[j - 1][k],A[j][k - 1])
    if j == k == N - 1:
        print(0)
        print (A[j][k])
        print (A) ##
        break
    elif k == N - 1:
        print(1)
        j = N - 1
        k = kstore + 1
        kstore = kstore + 1
    elif j == 0:
        print(2)
        j  = k + 1
        k = 0
    else:
        print(3)
        j = j - 1
        k = k + 1
    print ('cyc')
        
        
