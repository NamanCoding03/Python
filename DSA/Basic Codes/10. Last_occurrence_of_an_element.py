n = int(input())
arr=list(map(int,input().split()))
x=int(input())
if x not in arr:
   print(-1)
for i in range(n-1,0,-1):
    if arr[i]==x:
        print(i)
        break
