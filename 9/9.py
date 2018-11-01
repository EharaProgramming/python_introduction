# 関数

# function!!と表示するだけの関数
def func1() :
    print("function!!")

# 関数の実行
func1()

# 引数ありの関数 print("")
def func2(x) :
    y = x * 3
    print(y)

# 値を入れないと怒られる
# func2()

func2(4)

# 戻り値ありの関数
def func3(x, y) :
    z = x * y
    return z

a = func3(5, 4)
print(a)

# デフォルト引数
def func4(name="ななし") :
    print(name + "さん、おはようございます！")

func4()
func4('えはら')
