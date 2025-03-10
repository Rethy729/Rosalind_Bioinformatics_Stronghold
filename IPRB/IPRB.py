k = int(input())
m = int(input())
n = int(input())

def pro (a, b, c):
    s = float((a+b+c)*(a+b+c-1))
    d = float(2*a*b)
    e = float(2*b*c)
    f = float(2*c*a)
    g = float(a*(a-1))
    h = float(b*(b-1))
    
    z = (d/s)+(f/s) + ((e/s)*0.5) 
    y = (g/s)+(h/s)*(0.75)
    
    return z+y

print (pro(k, m, n))
