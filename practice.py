# クラス定義
class Human:
    # インスタンス変数
    name = None # 名前
    age = None  # 年齢
 
    # コンストラクタ
    def __init__(self):
        # do something
        print('コンストラクタが呼び出されました。')
 
    # クラスメソッド
    def printinfo(self):
        print('名前は{0}, 年齢は{1}' . format(self.name, self.age))
 
# インスタンス生成
human = Human()
human.name = 'taro'
human.age = 20
 
human.printinfo()


# クラス定義
class Human:
    # インスタンス変数
    name = None # 名前
    age = None  # 年齢
 
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('テスト')
 
    # クラスメソッド
    def printinfo(self):
        print('名前は{0}, 年齢は{1}' . format(self.name, self.age))
 
# インスタンス生成
human1 = Human('taro', 20)
human2 = Human('jiro', 40)
 
human1.printinfo()
human2.printinfo()