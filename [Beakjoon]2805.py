
lst = []
N , M = map(int,input().split())
lst = list(map(int,input().split()))
start, end = 1, max(lst)

    
while start<= end:
    mid = (start+end)//2
    x = 0
    for i in lst:
        if i >= mid:
            x += i-mid

    if x >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)




      









