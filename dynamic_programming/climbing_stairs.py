"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""

def climbing_stairs(n):
    def recur(num_steps, n):
        if num_steps == n:
            return 1
        if num_steps > n:
            return 0
        
        return recur(num_steps + 1, n) + recur(num_steps + 2, n)
    
    return recur(0, n)