# Simple integer operations in Python

# 1. Create integers
a = 10
b = 3

# 2. Basic arithmetic
print("Addition:", a + b)      # 13
print("Subtraction:", a - b)   # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor division:", a // b) # 3
print("Remainder:", a % b)       # 1
print("Power:", a ** b)          # 1000

# 3. Comparisons
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True

# 4. Convert between types
num_str = "42"
num = int(num_str)
print(num + 8)  # 50

float_num = 3.7
print(int(float_num))  # 3 (truncates decimal)

# 5. Math functions
import math
print("Square root:", math.sqrt(16))
print("Absolute value:", abs(-10))
print("Round:", round(3.14159, 2))  # 3.14

# 6. Random integer
import random
print("Random number (1–10):", random.randint(1, 10))
