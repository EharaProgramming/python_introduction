# 論理演算子
old = 65
child = 6

age = int(input())
if age <= child or age >= old :
    print("割引料金500円ください")
else :
    print("通常料金1300円ください")


num = int(input())
if num % 2 == 0 and num % 3 == 0 :
    print("２でも３でも割り切れる数値です")
else :
    print("それ以外の数値です")


if not age <= child :
    print("ジェットコースターに乗れます")

"""
OR演算子
条件式１ or 条件式２　 → １もしくは２がTrueの場合　Trueになる

AND演算子
条件式１ and 条件式2  → １と２両方がTrueの場合　Trueになる

NOT演算子
not 条件式 → 条件式がTrueの場合、False 条件式がFalseの場合Trueになる
"""
