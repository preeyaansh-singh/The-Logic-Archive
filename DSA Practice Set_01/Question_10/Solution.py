def climb_stairs(n):
    # Base cases: 1 way for 1 step, 2 ways for 2 steps
    if n <= 2:
        return n
        
    # Variables to track the previous two steps
    prev2 = 1  # Ways to reach step (n-2)
    prev1 = 2  # Ways to reach step (n-1)
    
    # Calculate ways for step 3 up to n
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return prev1

# Example Usage:
print(climb_stairs(4))  # Output: 5
