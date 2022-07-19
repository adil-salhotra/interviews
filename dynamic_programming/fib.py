
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n, memo=dict()):
    if n in memo: 
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def fibonacci_tab(n):
    tab = [0] * (n+1)
    tab[1] = 1

    for index in range(2,n+1):
        tab[index] = tab[index-1] + tab[index-2]
    
    return tab[n]