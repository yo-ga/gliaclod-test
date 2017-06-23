def c(n,r):
    ans = [[0 for x in range(r)] for y in range(n)] 
    for i in range(0,n):
        ans[i][0] = 1
        if i<r:
            ans[i][i] = 1
            ans[0][i] = 1
    for i in range(1,5,1):
        for j in range(1,3,1):
            if i == j or i ==1 or j==1:
                ans[i][j] = 1
            else:
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
    return ans[n-1][r-1]
print( c(5,3) )