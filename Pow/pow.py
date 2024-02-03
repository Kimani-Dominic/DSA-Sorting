# pow(x, n)

def pow(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = pow(x, n // 2)
        return half_power * half_power
       
    else:
        half_power = pow(x, (n-1) // 2)
        X = x * half_power * half_power
        return X

x = 2
n = 4
pow = 
print(pow(2, 4))