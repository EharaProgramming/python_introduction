# リスト
list1 = ["Banana", "Apple", "Tomate", 4000]

# リストを表示
print(list1)

# リストの各要素を表示する
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

# 0番目から3個目までを表示
print(list1[0:3])

# リストの0番目の要素に値を代入
list1[0] = "dddd"
print(list1)

# リストの中にリストを入れることも出来る
list2 = [list1, [1,2,3,""]]
print(list2)

# [['dddd', 'bbbb', 'cccc', 4], [1, 2, 3, '']]
print(list2[0][2])
print(list2[1][0])
