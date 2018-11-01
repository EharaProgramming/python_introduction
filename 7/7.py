# 辞書

dict = {"Ehara" : 2000 , "Masako" : 1990}
print (dict)

# キーを指定して値を取得できる
print(dict["Ehara"])

# keyを変数にすることも
key = "Masako"
val = dict[key]
print(val)

# キー：値の組み合わせを追加、変更も出来る
dict["Miwa"] = 2012
dict["Ehara"] = "ehara"
print(dict)


# for文での値の取得
for key in dict :
    print(key)
    print(dict[key])

# 値のみを取得
for val in dict.values() :
    print(val)
