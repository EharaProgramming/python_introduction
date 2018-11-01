# イテレータ

# まずはリストの確認
list = [1, 2, 3, 4, 5]
for i in list :
    if i < 3 :
        print(i)
    elif i == 3 :
        print(i)
        break

for i in list :
    print(i)

# リストからイテレータを生成
it = iter(list)
for i in it :
    if i < 3 :
        print(i)
    elif i == 3 :
        print(i)
        break

for i in it :
    print(i)
