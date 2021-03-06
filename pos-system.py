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
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    # １オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください
    # オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください
    # オーダー番号から商品情報を取得する（課題１）






    
    def item_name_price_from_order(self):
        for x in self.item_master:
            if item_code == x.item_code:
                return x.item_name, x.price







    def get_item_data(self,item_code):
        for m in self.item_master:
            if item_code==m.item_code:
                return m.item_name,m.price

    
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



'''



#1 オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください
★



【まずやることの確認】
① UTF-8 withBOM
② venvの設定
③ gitignoreの設定
④ pip3 installでインストール（課題4はなし？）



【わからないこと】

① def main()のインデント。
→この関数はどのクラスにも属していないということ？

② 引数の扱い。
・そもそも論。
・何のための引数？
・関数の定義と実行では、引数の数が同じでは？

③ 関数のそれぞれの役割。



'''