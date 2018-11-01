# 集合（set型）

# 宣言
set = {1, 2, 3}
print(set)
print(type(set))

# 要素の追加
set.add(4)
print(set)

# 要素の取得
# リストとは違い、順番通り値が入っているとは限らないので
# インデックス参照はできない
# print(set[0])

for val in set :
    print(val)


set1 = {1, 2, 3, 4}
set2 = {1, 3, 5, 7}

# 和集合
# 1, 2 どちらかに存在している値を格納
set = set1 | set2
set = set1.union(set2)
print(set)

# 積集合
# 1, 2 どちらにも存在している値を格納
set = set1 & set2
set = set1.intersection(set2)
print(set)

# 差集合
# 1 から 2 の値を削除した値を格納
set = set1 - set2
set = set1.difference(set2)
print(set)

# 排他的論理和集合
# 1, 2 どちらにも存在している値を削除
set = set1 ^ set2
set = set1.symmetric_difference(set2)
print(set)
