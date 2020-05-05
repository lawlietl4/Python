import random
import statistics
from statistics import mean, mode, median, stdev

numbers = [x for x in range(1,501)]

print("\nthe mean is: ", mean(numbers))
print("the mode is: ", mode(numbers))
print("the maximum is: ", max(numbers))
print("the minimum is: ", min(numbers))
print("the standard deviation is: ", stdev(numbers))

numbers = [random.randint(1,100) for x in range(1,501)]

random.shuffle(numbers)

print("\nthe mean is: ", mean(numbers))
print("the mode is: ", mode(numbers))
print("the maximum is: ", max(numbers))
print("the minimum is: ", min(numbers))
print("the standard deviation is: ", stdev(numbers))