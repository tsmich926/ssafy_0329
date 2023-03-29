def binaryS(A,keys,key):
    global cnt
    m = len(A)//2
    l = 0
    r = len(A)-1
    if A[m] > key : #찾고자 하는 수보다 중간 인덱스의 값이 크면
        for i in range(l,m):
            if A[i] == key:
                cnt += 1
            else:


    if A[m] == key: #찾고자 하는 값이 중간 인덱스 값일때
        cnt +=1

    else: #중간 인덱스의 값이 찾는 값보다 더 작을때
        for i in range(m+1,r+1):
            if A[i] == key:
                cnt += 1
            else:


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    keys = list(map(int,input().split()))
    cnt = 0
    for key in keys:
        if binaryS(A,keys,key):
            lst.append(key)
    if len(lst)==0:
        ans = 0
        print(f'{tc} {ans}')
    else:
        print(*lst)