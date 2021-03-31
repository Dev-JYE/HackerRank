n = int(input())
arr = list(map(int, input().split()))
rscore=0
for i in range(n):
    if (arr[i])<max(arr):
        rscore=arr[i]
        if arr[i]>rscore:
            rscore=arr[i]
print(rscore)
#해결 못함,,,다시 풀자
