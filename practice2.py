"""
###1 インスタンスを生成し、クラスのsay()メソッドを呼び出す例。
class Greeting():
    def say(self):
        print('Hello World!!')

x = Greeting()
x.say()



###2 引数があるメソッドの定義。名前と年齢を格納するインスタンス変数を、クラスに宣言する例。
class Data:
    name = None
    age = None

    def say(self):
        print('名前:{0}、 年齢：{1}' .format(self.name, self.age))

# 1つめのインスタンス
x = Data()
x.name = '山田'
x.age = 20

# 2つめのインスタンス
y = Data()
y.name = '鈴木'
y.age = 100

x.say()
y.say()



###3 コンストラクタ
class Fruits:
    fruits = []
    
    def __init__(self):
        print('コンストラクタが呼び出されました。')
        #初期化
        self.fruits.append('りんご')
        self.fruits.append('みかん')
        self.fruits.append('ぶどう')

f = Fruits()
print(f.fruits)



###4 継承
class Abc:
    abc = '継承元のインスタンス変数'

    def abc_function(self):
        print('abc_function = ' + self.abc)

# Abcを継承したDefgクラス
class Defg(Abc):
    defg = '継承先のインスタンス変数'

    def defg_function(self):
        print('defg_function= :' + self.abc)
        print('defg_function= :' + self.defg)

x = Defg()
x.abc_function()
x.defg_function()



# インスタンス化のときに引数を加える。
class Person(): #クラス名
    def __init__(self, name): #インスタンス化メソッド
        self.name = name

    def hello(self):
        print("Hello! I am {}.".format(self.name))

Peter = Person('太郎')
Peter.hello()

Mary = Person('Mary')
Mary.hello()

"""
# 引数のおさらい
# ①引数なし関数

def hello():
    print ('Hello')
hello()   # Hello

# ②引数あり関数ー１
def hello(name):
    print ('Hello '+ name)
hello('Sato')   # Hello Sato

# ③引数あり関数ー２
def abc(a, b):
    x = a + b
    return x
answer = abc(70, 30)
print (answer)