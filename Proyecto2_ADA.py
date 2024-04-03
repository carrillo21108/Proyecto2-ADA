# Numero de pasos realizados
cant_pasos = 0

# Enfoque DaC
def lcs_dac(A, B, i, j):
    global cant_pasos
    cant_pasos+=1
    
    if i == 0 or j == 0:
        return 0
    elif A[i-1] == B[j-1]: 
        return 1 + lcs_dac(A, B, i-1, j-1) 
    else: 
        return max(lcs_dac(A, B, i-1, j), lcs_dac(A, B, i, j-1)) 
  
# Enfoque Programacion Dinamica    
def lcs_pd(A, B, i, j, dp): 
    global cant_pasos
    cant_pasos+=1
    
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


A = "AGGTAB"
B = "GXTXAYB"
  
m = len(A) 
n = len(B) 
dp = [[-1 for i in range(n+1)]for j in range(m+1)] 
  
print("Longitud de LCS con enfoque DaC: ", lcs_dac(A, B, m, n))
print("Tiempo de ejecucion: ", cant_pasos)
input("Presione [Enter] para continuar\n")

cant_pasos=0
print("Longitud de LCS con enfoque PD: ", lcs_pd(A, B, m, n, dp))
print("Tiempo de ejecucion: ", cant_pasos)