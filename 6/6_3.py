# ループ処理応用

# if文と組み合わせ
for i in range(0, 10) :
    if i == 2 :
        print("2です")
    else :
        print("2じゃないです")

i = 0
while i < 10 :
    if i == 2 :
        print("2です")
    else :
        print("2じゃないです")
    print(i)
    i += 1

# break文
for i in range(0, 10) :
    if i == 2 :
        break
    print(i)

# continue文
for i in range(0, 10) :
    if i == 2 :
        continue
    print(i)
