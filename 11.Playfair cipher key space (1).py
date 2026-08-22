import math

# Total possible keys (25 letters because I/J are combined)
total_keys = math.factorial(25)

# Approximate power of 2
power = math.log2(total_keys)

print("Total Possible Keys =", total_keys)
print("Approximate = 2^", round(power, 2))

# Effective unique keys
effective_keys = total_keys // 2

print("Effective Unique Keys =", effective_keys)
print("Approximate = 2^", round(math.log2(effective_keys), 2))
