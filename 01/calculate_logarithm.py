a, b = map(int, input().split())

def ln(x):
    val = x
    return 99999999*(x**(1/99999999)-1)

def log(x, base):
    r = ln(x) / ln(base)
    return r
    
result = log(a, b)
print(f"{result:.2f}")
