# リスト以外の内包表記

# 辞書
dict = {str(i):i * 2 for i in range(100) if i % 2 == 0}
print(dict)
print(type(dict))

# 集合
set = {i * 2 for i in range(100) if i % 2 == 0}
print(set)
print(type(set))

# ジェネレータ
gen = ( i * 2 for i in range(100) if i % 2 == 0)
for val in gen :
    print(val)

for val in gen :
    print(val)
print(type(gen))
