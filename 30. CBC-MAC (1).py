x = int(input("Enter block X: "))

t = x ^ 123

print("MAC =", t)

second = x ^ t

print("Second Block =", second)

print("CBC-MAC for X||(X XOR T) can be forged.")
