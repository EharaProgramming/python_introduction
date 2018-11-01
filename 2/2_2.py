# 文字列

# 文字列はダブルクォーテーションで囲ってあげる
str1 = "mojiretu"
print(str1)

# 複数行にまたがる場合
str2 = """sssssss
bbbbbbbbbbbbbb
aaaaaaa"""
print(str2)

# 日本語も書けます
str3 = "侍"
print(str3)

# シングルクォーテーション
str4 = 'wwwww'
print(str4)

# pythonでは、シングルクオーテーションも
# ダブルクォーテーションも扱いが同じ
print(type(str4))

# 文字列の連結
strstr = "a" + "b"
print(strstr)

# 連結は変数同士でもできます。
str13 = str1 + str3
print(str13)

# 複雑な連結
print(str13 + str4)

# 数値の文字列
str5 = "1"
print(str5)
print(type(str5))

# 数値と文字列を足し算すると・・・
print(1 + "1")
