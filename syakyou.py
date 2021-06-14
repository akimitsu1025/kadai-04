import pandas as pd

### 商品クラス
class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price

    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self, item_master):
        self.item_order_list = []
        self.item_master = item_master

    def add_item_order(self, item_code):
        self.item_order_list.append(item_code)

    def view_item_list(self):
        for item in self.item_order_list:
            print('商品コード:{}'.format(item))

    # １オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください
    def get_item_data(self):
        for xxx in self.item_order_list:
            for yyy in self.item_master:
                if yyy.item_code == xxx:
                    print(yyy.item_name, yyy.price)
                    break
    
    # 2オーダーをコンソール（ターミナル）から登録できるようにしてください。登録時は商品コードをキーとする
    def input_order(self):
        print('いらっしゃいませ！')
        buy_item_code = input('購入したい商品のコードを入力してください。（001 or 002 or 003 or 004 or 005）：')
        if buy_item_code in ["001", "002", "003", "004", "005"]:
            print('{}が登録されました。'.format(buy_item_code))
            #4 オーダー登録時に個数も登録できるようにしてください
            while True:
                buy_item_code = input("購入したい商品を入力してください。登録を完了する場合は、0を入力してください >>> ")
                if int(buy_item_code) != 0:
                # マスタに存在するかチェック(課題外：カスタマイズ)
                check = self.get_item_data(buy_item_code)
                if check != None:
                    print("{} が登録されました".format(check[0]))
                    buy_item_count = input("個数を入力してください　>>> ")
                    self.add_item_order(buy_item_code,buy_item_count)
                else:
                    print("「{}」は商品マスタに存在しません".format(buy_item_code))
            else:
                print("商品登録を終了します。")
                break

### メイン処理
def main():
    # マスタ登録
    item_master = []
    item_master.append(Item('001', 'りんご', 100))
    item_master.append(Item('002', 'なし', 120))
    item_master.append(Item('003', 'みかん', 150))

    # オーダー登録
    order = Order(item_master)
    order.add_item_order('001')
    order.add_item_order('002')
    order.add_item_order('003')

    # オーダー表示
    #order.view_item_list()
    order.get_item_data()
    order.input_order()

if __name__ == '__main__':
    main()

"""
★メソッド名を回答に合わせる。

回答コード
def input_order(self):
        print("いらっしゃいませ！")
        while True:
            buy_item_code=input("購入したい商品を入力してください。登録を完了する場合は、0を入力してください >>> ")
            if int(buy_item_code)!=0:
                # マスタに存在するかチェック(課題外：カスタマイズ)
                check=self.get_item_data(buy_item_code)
                if check!=None:
                    print("{} が登録されました".format(check[0]))
                    buy_item_count=input("個数を入力してください　>>> ")
                    self.add_item_order(buy_item_code,buy_item_count)
                else:
                    print("「{}」は商品マスタに存在しません".format(buy_item_code))
            else:
                print("商品登録を終了します。")
                break

俺のコード
def registration(self):
        input_code = input('購入したい商品のコードを入力してください。（001 or 002 or 003 or 004 or 005）：')
        if input_code in ["001", "002", "003", "004", "005"]:
            print('{}が登録されました。'.format(input_code))
            #4 オーダー登録時に個数も登録できるようにしてください
            input_count = input('個数を入力してください。：')
            print('{}個購入します。'.format(input_count))
        else:
            print('正しいコード（001 or 002 or 003 or 004 or 005）を入力してください。')

"""