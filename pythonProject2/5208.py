# 바이너리 카운팅
arr = [3,6,7,1,5,4]
n = len(arr)

for i in range(0, (1<<n)): # 부분집합의 개수만큼 print
    for j in range(0, n):  # 원소의 수만큼 비트를 비교함
        if i & (1<<j):     # i의 j번째 비트가 1이면 원소 출력
            print(arr[j], end = ' ')
    print()



# def dfs(i,tmp):
#
#
#
# T = int(input())
# for tc in range(1,T+1):
#     lst = list(map(int,input().split()))
#     num = lst[0]
#     stops = lst[1:]
#     for i in range(num):

