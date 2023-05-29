# myset = set()
#
# myset.add(1)
# myset.add(2)
# myset.add(3)
#
# print(myset.pop())
# print(myset)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8, }
primes = {2, 3, 5, 7, 11}

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)

u = evens.union(primes)
print(u)

i = primes.intersection(odds)
print(i)