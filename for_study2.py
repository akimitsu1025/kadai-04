import pandas as pd

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_count_list=[]
        self.item_master=item_master
    
    def add_item_order(self, item_code, item_count):
        self.item_order_list.append(item_code)
        self.item_count_list.append(item_count)

    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    #1 オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください
    def print_list(self):
        for xxx in self.item_order_list:
            for yyy in self.item_master:
                if yyy.item_code == xxx:
                    print(yyy.item_name, yyy.price)
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
def main():
    item_master = master_registration()

    # オーダー登録
    order=Order(item_master)
  
    # オーダー表示
    order.view_item_list()
    order.registration()
    order.print_list()

if __name__ == "__main__":
    main()