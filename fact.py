def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))



l = [1, 2, 4]

for i in range(10):
    print(i)
