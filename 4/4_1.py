# リストの関数
list1 = ["Banana", "Apple", "Tomate", 4000]
print(list1)

# 要素の追加
list1.append("dddd")
print(list1)

# リストの結合  list += ["z","c","v","b"]
list1.extend(["z","c","v","b"])
print(list1)

# 指定した場所に要素を挿入
list1.insert(4, "n")
print(list1)

# 要素の削除 関数ではない
del list1[4]
print(list1)

# 要素の削除　値指定
list1.remove("Banana")
print(list1)

# 要素を取り出して削除 デフォルトは indexが-1
val = list1.pop(0)
print(val)
print(list1)

# ソート float型も自動で判別してくれる
list2 = [100, 222, 231, 1233, 100.1, -123]
print(list2)
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)

# リストの要素数を取得
len = len(list2)
print(len)
