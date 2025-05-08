###variant44
import itertools

n = int(input())
list2 = list(itertools.permutations(range(1, n+1)))

print(len(list2))

for finish in list2:
    print(' '.join(map(str, finish)))
