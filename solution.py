#Function should return an integer
#You may use python modules
from itertools import permutations
MOD = 10**9+7
def getSum(n, arr):
    #Code here
    arr=list(map(str,arr))
    s=''
    su=0
    for val in (permutations(arr,n)):
        s=''.join(val)
        su+=int(s)
    return(su%MOD)
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        arr = list(map(int, input().strip().split()))
        print(getSum(n, arr))
#contributed By: Harshit Sidhwa
# } Driver Code Ends
