# エラー処理

# 0除算
x = 1
y = 0

try :
    # z = x / y
    # raise SyntaxError
    print("エラーは発生しません")
except ZeroDivisionError :
    print("0除算のエラーが発生しました！")
except SyntaxError :
    print("Pythonの構文エラー！")
else :
    print("エラーが発生しなかった場合に行う処理")
finally :
    print("エラーの発生有無にかかわらず行う処理")

print("何らかの処理")
