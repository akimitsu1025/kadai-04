# コメントアウトを最小限に。

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
        self.item_master=item_master

    def add_item_order(self,input_code, input_count):
        self.item_order_list.append(input_code)
        self.item_order_list.append(input_count)
        
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
    
    
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    
    # オーダー登録
    order=Order(item_master)
    order.add_item_order("001")
    order.add_item_order("002")
    order.add_item_order("003")
    
    # オーダー表示
    order.view_item_list()
    
if __name__ == "__main__":
    main()



"""
①add_item_orderの引数を変更。
def add_item_order(self,item_code):
def add_item_order(self,input_code, input_count):

その下の行
self.item_order_list.append(item_code)
self.item_order_list.append(input_code)

"""