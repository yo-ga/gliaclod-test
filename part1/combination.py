def c(n,r):
    ans = [[0 for x in range(r)] for y in range(n)] 
    for i in range(0,n):
        ans[i][0] = i+1
        if i<r:
            ans[i][i] = 1
    for i in range(0,n):
        for j in range(0,r):
            if ans[i][j] == 0:
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
    return ans[n-1][r-1]
print( c(990,33) )