import itertools
k=0
for i in itertools.product('ИВАН', repeat=5):
    if i.count('И') >= 1:
        k+=1
print(k)
