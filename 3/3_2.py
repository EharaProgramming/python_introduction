#elif else

a = 5
b = 5

if a <= b :
    print("a は b 以下")
elif a >= b :
    print("a は b 以上")
else :
    print("どちらでもないよ")

# if a <= b :
#     print("a は b 以下")
# if a >= b :
#     print("a は b 以上")

# 入力してもらう
bmi = int(input())
if bmi < 18 :
    print("もっとごはん食べて！")
elif bmi <= 25 :
    print("標準ですね！")
elif bmi < 100 :
    print("一緒に頑張りましょう！")
else :
    print("ひえええええええええええ！！")

"""
if 条件式１ :

    処理１
elif 条件式2 :
    処理２
else :
    処理３
"""
