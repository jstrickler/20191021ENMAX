
LIMIT = 100
LIMIT += 1 # take care of 0-based stuff

is_prime = [True] * LIMIT

print(is_prime)

for n in range(2, LIMIT):
    if is_prime[n]:
        print(n, end=', ')
        for j in range(n * 2, LIMIT, n):
            is_prime[j] = False
print()
print(is_prime)