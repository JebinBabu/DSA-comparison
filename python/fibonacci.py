# Finding finoncci number for next n numbers using loop

n = 18

prev2 = 0
prev1 = 1

print(prev2)
print(prev1)

for fibo in range(n):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo


# Finding fibonacci using recursion

print(0)
print(1)
count = 1

def fibonacci(prev1, prev2):
    global count
    if count <= n:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)

        