M = 0 
for i in range(84052, 84131):
    delitely = 2
    for j in range(2, i//2 + 1):
        if i % j == 0:
            delitely += 1
    if delitely > M:
        M = delitely
        m = i
print(M, m)
