# ジェネレータ

# ジェネレータ return ではなく yield
def gen1() :
    for val in [1, 2, 3, 4, 5] :
        yield val

# イテレータになる
g1 = gen1()

# 実験 ジェネレータ
for i in g1 :
    if i < 3 :
        print(i)
    elif i == 3 :
        print(i)
        break

for i in g1 :
    print(i)
