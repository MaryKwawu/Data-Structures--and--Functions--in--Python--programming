# myset = set()
#
# myset.add(1)
# myset.add(2)
# myset.add(3)
#
# print(myset.pop())
# print(myset)

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8, }
# primes = {2, 3, 5, 7, 11}
#
# u = odds.union(evens)
# print(u)
#
# i = evens.intersection(primes)
# print(i)
#
# u = evens.union(primes)
# print(u)
#
# i = primes.intersection(odds)
# print(i)

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# diff = setA.difference(setB)
# diff = setB.difference(setA)
# diff = setB.symmetric_difference(setA)
# diff = setA.symmetric_difference(setB)

# setA.update(setB)
# setB.update(setA)
# setA.difference_update(setB)
# setB.difference_update(setA)

# setA.symmetric_difference_update(setB)
# print(setA)

# setA = {1, 2, 3, 4, 5}
# setB = {1, 2, 3, 4}
# setC = {7, 8}

# setB = setA
# setA = setB
# setB = setA.copy()
# setB = set(setA)
# setB.add(7)
# print(setA)
# print(setA.isdisjoint(setB))
# print(setA.isdisjoint(setC))
# print(setB.issubset(setA))
# print(setA.issubset(setB))
# print(setB.issuperset(setA))
# print(setA.issuperset(setB))

a = frozenset([1, 2, 3, 4])
print(a)

