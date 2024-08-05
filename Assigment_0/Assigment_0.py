import math
import random
import sys
def successors(cinit):
    # A better successors function
    arr = [cinit + random.randint(-5, 5) for _ in range(20)]
    return arr
def value(c):
    return c**2-22*c
# Implement the simulated annealing search
def simulated_annealing(tmax,tmin,cinit):
    current = cinit
    for t in range(tmin,tmax):
        T = 1/t
        next_state = random.choice(successors(current))
        delta_e = value(next_state) - value(current)
        if delta_e > 0 or math.exp(delta_e / T) > random.random():
            current = next_state
    return current
# Create an instance of the Problem class
tmax=1000
tmin=1
cinit=0
# Run the simulated annealing search

result = simulated_annealing(tmax,tmin,cinit)

# Print the result
print("The result of the simulated annealing search is:", result)
