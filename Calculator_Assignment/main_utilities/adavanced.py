def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result


def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
