
"""
def k_gen_matrix(k):
    #AABB, AaBB, aaBB, AABb, AAbb, AaBb, Aabb, aaBb, aabb
    matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if k == 1:
        matrix[5] = 1
        return matrix

    alpha = float(4*(k_gen_matrix(k-1)[0]) + 2*(k_gen_matrix(k-1)[1]) + 2*(k_gen_matrix(k-1)[3]) + k_gen_matrix(k-1)[5])/4
    beta = float(4*(k_gen_matrix(k-1)[4]) + 2*(k_gen_matrix(k-1)[3]) + 2*(k_gen_matrix(k-1)[6]) + k_gen_matrix(k-1)[5])/4
    gamma = float(4*(k_gen_matrix(k-1)[2]) + 2*(k_gen_matrix(k-1)[1]) + 2*(k_gen_matrix(k-1)[7]) + k_gen_matrix(k-1)[5])/4
    delta = float(4*(k_gen_matrix(k-1)[8]) + 2*(k_gen_matrix(k-1)[6]) + 2*(k_gen_matrix(k-1)[7]) + k_gen_matrix(k-1)[5])/4
    
    matrix[0] = float(0.25) * alpha
    matrix[1] = float(0.25) * (alpha + gamma)
    matrix[2] = float(0.25) * gamma
    matrix[3] = float(0.25) * (alpha + beta)
    matrix[4] = float(0.25) * beta
    matrix[5] = float(0.25) * (alpha + beta + gamma + delta)
    matrix[6] = float(0.25) * (beta + delta)
    matrix[7] = float(0.25) * (gamma + delta)
    matrix[8] = float(0.25) * delta

    return matrix
    
"""


memo = {1:1}

def factorial(a):
    if a in memo:
        return memo[a]
    else:
        res = a*factorial(a-1)
        memo[a] = res
        return res
    
k = int(input())
n = int(input())
factorial(2**k)
memo[0] = 1

p_sum = 0
p = float(0.25)
for i in range(n, (2**k)+1):    
    c = float(memo[2**k]/float(memo[i] * memo[2**k - i]))
    p_sum = p_sum + (c * (p**i) * ((1-p)**(2**k - i)))

print (round(p_sum, 3))

