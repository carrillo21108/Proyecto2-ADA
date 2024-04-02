# Enfoque DaC
def lcs_dac(A, B, i, j): 
    if i == 0 or j == 0: 
        return 0
    elif A[i-1] == B[j-1]: 
        return 1 + lcs_dac(A, B, i-1, j-1) 
    else: 
        return max(lcs_dac(A, B, i-1, j), lcs_dac(A, B, i, j-1)) 
  
# Enfoque Programacion Dinamica    
def lcs_pd(A, B, i, j, dp): 
    if (i == 0 or j == 0): 
        return 0
    elif (dp[i][j] != -1): 
        return dp[i][j] 
    elif A[i-1] == B[j-1]: 
        dp[i][j] = 1 + lcs_pd(A, B, i-1, j-1, dp) 
        return dp[i][j] 
    else:
        dp[i][j] = max(lcs_pd(A, B, i-1, j, dp), lcs_pd(A, B, i, j-1, dp)) 
        return dp[i][j] 
# Main
if __name__ == '__main__': 
    A = "AGGTAB"
    B = "GXTXAYB"
  
    m = len(A) 
    n = len(B) 
    dp = [[-1 for i in range(n+1)]for j in range(m+1)] 
  
    print("Longitud de LCS con enfoque DaC: ", lcs_dac(A, B, m, n))
    print("Longitud de LCS con enfoque PD: ", lcs_pd(A, B, m, n, dp))