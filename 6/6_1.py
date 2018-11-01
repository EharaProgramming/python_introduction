#for文

# range → 整数のリストを自動で生成する関数
# リスト内の各要素に対して継続的に処理を行うことが出来る
for i in range(3) :
    print(i)

# 上記プログラムと同様
for i in [0, 1, 2]:
    print(i)

# 1から始まる整数を3つ生成
for i in range(1, 3) :
    print(i)


# 文字列取得
list1 = ["Hello", "my", "name", "is"]
for str in list1 :
    print(str)
