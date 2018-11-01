# リストの内包表記

# 通常
list = []
for i in range(3) :
    list.append(i)
print(list)

# 内包表記
list = [i for i in range(3)]
print(list)

# 条件分岐と組み合わせることが出来る
# 通常
list = []
for i in range(200) :
    if i % 2 == 0 and i % 3 == 0 :
        list.append(i)
print(list)

# 内包表記
list = [i for i in range(200) if i % 2 == 0 and i % 3 == 0]
print(list)
