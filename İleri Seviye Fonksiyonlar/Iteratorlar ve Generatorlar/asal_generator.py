
def asallar():
    yield 1
    yield 2

    # range(3,1000+1) --> i / range(2,i) --> j / i%j==0: return False

    for i in range(3,1001):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i

gen = asallar()

for i in gen:
    print(i)










