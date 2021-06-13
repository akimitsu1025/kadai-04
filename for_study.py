import pandas as pd

### 商品クラス
class Item: # Itemクラスの定義。
    def __init__(self,item_code,item_name,price): # コンストラクタで初期設定。第１引数にself。第２引数にitem_code。第３引数にitem_name。第４引数にprice。
        self.item_code=item_code # この表記がわからない。変数self.item_codeに引数item_codeを代入？
        self.item_name=item_name # この表記がわからない。変数self.item_nameに引数item_nameを代入？
        self.price=price         # この表記がわからない。変数self.priceに引数priceを代入？
    
    def get_price(self): # get_priceメソッドの定義。引数はselfのみ。→何のためのメソッド？
        return self.price # 6行目のself.priceを返す？

### オーダークラス
class Order: # Orderクラスの定義。引数はなくて大丈夫？
    def __init__(self,item_master): # コンストラクタで初期設定。第１引数にself。第２引数にitem_master。
        self.item_order_list=[] # self.item_order_listに空のリストを用意？何のために？ここにorderの情報が入っている。
        self.item_count_list=[] # 自分のコード。回答を見て追加。
        self.item_master=item_master # 変数self.item.masterに引数item_masterを代入？
    
    def add_item_order(self, item_code, item_count): # add_item_orderメソッドの定義。第１引数にself。第２引数にitem_code。第２引数は自分のコード。回答を見て追加。
        self.item_order_list.append(item_code) # 空リストで用意したself.item_order_listにitem_codeを追加する。item_codeとはadd_item_orderメソッドで定義した関数の引数。。。どういう関係？
        self.item_count_list.append(item_count) #自分のコード。回答を見て追加。

    def view_item_list(self): # view_item_listメソッドの定義。引数はselfのみ。→何のためのメソッド？
        for item in self.item_order_list: # 変数itemにself.item_order_listを代入して繰り返し処理。self.item_order_listとは14行目で定義（準備？）した空リスト？
            print("商品コード:{}".format(item)) # 「商品コード:変数item」とprint。

    #1 オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください
    def print_list(self):
        for xxx in self.item_order_list:           # オーダーをループ処理。：self.item_order_listをループ処理。001とか。
            for yyy in self.item_master:           # self.item_masterをループ処理。この2行がいまいちよくわからない。for y in self.item_order_list: からのfor x in self.item_master:。。？
                if yyy.item_code == xxx:             # 取り出したマスターを元に、コードを検索して商品名、価格名を表示させる。
                    print(yyy.item_name, yyy.price)  #
                    break

    #2 オーダーをコンソール（ターミナル）から登録できるようにしてください。登録時は商品コードをキーとする
    def registration(self):
        input_code = input('購入したい商品のコードを入力してください。（001 or 002 or 003 or 004 or 005）：')
        if input_code in ["001", "002", "003", "004", "005"]:
            print('{}が登録されました。'.format(input_code))
            #4 オーダー登録時に個数も登録できるようにしてください
            input_count = input('個数を入力してください。：')
            print('{}個購入します。'.format(input_count))
        else:
            print('正しいコード（001 or 002 or 003 or 004 or 005）を入力してください。')

    #5 オーダー登録した商品の一覧（商品名、価格）を表示し、かつ合計金額、個数を表示できるようにしてください
    # →「オーダー登録した商品の一覧（商品名、価格）を表示」は#1と同じ処理では？
#    def view_order(self):
#        for item_order in self.item_order_list:
#            print(self.print_list(item_order))







"""
# 米谷さんコード
 def view_order(self):
        number=1
        self.sum_price=0
        self.sum_count=0
        self.receipt_name="receipt_{}.log".format(self.datetime)
        self.write_receipt("-----------------------------------------------")
        self.write_receipt("オーダー登録された商品一覧\n")
        for item_order,item_count in zip(self.item_order_list,self.item_count_list):
            result=self.get_item_data(item_order)
            self.sum_price+=result[1]*int(item_count)
            self.sum_count+=int(item_count)
            receipt_data="{0}.{2}({1}) : ￥{3:,}　{4}個 = ￥{5:,}".format(number,item_order,result[0],result[1],item_count,int(result[1])*int(item_count))
            self.write_receipt(receipt_data)
            number+=1
"""




#3 商品マスタをCSVから登録できるようにしてください
def master_registration():
    df = pd.read_csv('./master.csv')
    x = list(df["商品コード"])
    y = list(df["商品名"])
    z = list(df["価格"])
    item_master = []
    for xx, yy, zz in zip(x, y, z):
        item_master.append(Item(xx, yy, zz))
        return item_master

### メイン処理
def main(): # main関数の定義。インデントされていないので、これはOrderクラスのメソッドではない？
    # マスタ登録
#    item_master=[] # 変数item_masterに空の空のリストを用意。何のために？これがインスタンス化？
#    item_master.append(Item("001","りんご",100)) # 31行目で定義したitem_masterにItemクラスを追加。引数は３つ。どういう意味？
#    item_master.append(Item("002","なし",120))   # 31行目で定義したitem_masterにItemクラスを追加。引数は３つ。どういう意味？
#    item_master.append(Item("003","みかん",150)) # 31行目で定義したitem_masterにItemクラスを追加。引数は３つ。どういう意味？
    item_master = master_registration()

    # オーダー登録
    order=Order(item_master) # インスタンス化。変数orderにOrderクラスを代入。引数の扱いがよくわからない。
#    order.add_item_order("001") # 37行目で定義した変数orderに17行目で定義したadd_item_orderメソッドを追加。引数は１つ？引数の扱いがよくわからない。
#    order.add_item_order("002") # 37行目で定義した変数orderに17行目で定義したadd_item_orderメソッドを追加。引数は１つ？引数の扱いがよくわからない。
#    order.add_item_order("003") # 37行目で定義した変数orderに17行目で定義したadd_item_orderメソッドを追加。引数は１つ？引数の扱いがよくわからない。
    
    # オーダー表示
    order.view_item_list() # 37行目で定義した変数orderに20行目で定義したview_item_listメソッドを追加。引数はなくていいのか？
    order.registration()
    order.print_list()
#    order.view_order()


if __name__ == "__main__": # pyファイルとして実行されているかを確認する定型文。
    main()



'''
① まずやることの確認
１ UTF-8 with BOM
２ venvの設定
３ gitignoreの設定
４ pip3 installでライブラリをインストール（課題4ではpandasだけ？）

② venvはフォルダごとで反映されるのか？
　ファイルごとに作成、有効化する必要はない？
　python3 -m venv venv
　. venv/bin/activate

③ 「pip3 install〜」はファイルごとにする必要がある？

④ gitignoreの追加方法。
コマンドパレットでgitignoreを追加したが、ファイルが何も書かれていない。
参考サイト：https://opcdiary.net/gitignore-extension-for-visual-studio-code/

⑤ メソッドにつく引数の使い方がわからない。
例）def __init__(self,item_code,item_name,price)
　　def __init__(self,item_master)
　　def add_item_order(self,item_code)
　　def view_item_list(self)
。。。
コンストラクタ__init__の引数と自作関数の引数、それぞれ役割が違うのか？
selfの使い方がよくわからない。
コンストラクタでよくみられる表記。
def __init__(self, 第２引数):
    self.第２引数 = 第２引数
。。。
例）3〜6行目。
def __init__(self, item_code, item_name,price):
    self.item_code = item_code
    self.item_name = item_name
    self.price = price　　　←「self.price」と「price」の違いは？

★ selfのみの場合は？
　def view_item_list(self): 

★ __init__以外のメソッドにつく引数は？
　def add_item_order(self,item_code):
    その後、「self.item_code = item_code」とはなっていない。



〜課題１：オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください〜

【わからないこと】
・オーダー登録した商品とは？mainの中のマスタ登録のことか？.appendで追加されているりんご、なし、みかんのこと？
・コードを書く場所は？回答ではmain()の処理の前に記述されている。
・コードの表記は？回答を見ても理解できなかった。。

【やったこと：できなかった】
・一覧表示のためにメソッドを作成。
・self.item_masterの引数は３つずつなので、for文の中に3つの変数を用意して繰り返し処理。

def print_list(self):
    for x, y, z in self.item_master:
    print(x, y, z)
これでxに商品コードが、yに商品名が、zに価格が代入されるのでは。。？
その後の呼び出しは「order.print_list()」としたが、エラーになる。



〜課題２：オーダーをコンソール（ターミナル）から登録できるようにしてください
登録時は商品コードをキーとする〜

【わからないこと】
・コードを書く場所
・コードの表記
・作成した関数と別の関数（もしくはクラス）との連携。

【やったこと】
・メソッドを作成
・inputを使う

def registration(self):
    input_code = input('商品コードを入力してください。（001 or 002 or 003）：')
    if input_code == 001, 002, 003:
        print('{}が登録されました。'.format(input_code))
    else:
        print('正しいコード（001 or 002 or 003）を入力してください。')



〜課題３：商品マスタをCSVから登録できるようにしてください〜

【やろうとしていること】
Pandasを使って、read_csv。




★ def main()のインデント。
→この関数はどのクラスにも属していないということ？

'''