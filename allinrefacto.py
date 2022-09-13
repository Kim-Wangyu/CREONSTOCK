
#### 다른 스토어가 생긴다면 ?
#1. 스토어를 추상화한다.
#2. 스토어들이 늘어나면, 스토어가 그랩스토어만 가진다. 외부에서 주입 받을 수 있도록 의존성 주입을 한다


#### 

#3. 유저가 많은 행위를 책임지고 있다. Store가 판매하는 책임을 가져야 한다.
#개선점
#1.상점에서 상품을 판매하는 행위를 추상화하고 구체적인 로직을 해당 메서드로 옮긴다.

#4번prodict가 책임을 가져야 하지 않을까?
#개선점
#1. 딕셔너리 타입을 클래스(데이터클래스)객체로 변환하자.

from abc import ABC, ABCMeta, abstractmethod
from cgi import print_exception
from dataclasses import dataclass
from typing import Dict

@dataclass          #클래스에서 데이터를 넣을때 생성자를 생성하는데, dataclass를 이용하면 좀 더 쉽게 넣을 수 있게 도와줌
class Product:
    name: str       #어떤타입이고 어떤필드가 드러가는지 확인가능
    price:int

# product=Product(name=name,price=print)  이렇게
# product.name




class Store(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self._money = 0   #원래는 구체적인 값,코드가이 들어가면 안되지만 파이썬에서는 추상클래스에서는 이렇게 구현을 한다. 
        self.name= ""
        self._products={}

    @abstractmethod
    def show_product(self,product_id):
        pass

    @abstractmethod
    def sell_product(self,product_id,money):
        pass


class GrabStore(Store): #  +(Store) 인터페이스를 구현했다고 봐도됨 
    def __init__(self,products):
        self._money =0
        self.name = "그랩마켓"
        self._products=products

    def set_money(self,money:int):
        self._money = money

    def set_products(self,products:Dict[int,Product]): #def set_products(self,products:Dict[int,Product]): 이렇게 바꿔야함 원래
        self._products = products

    def show_product(self,product_id):
        return self._products[product_id]

    def sell_product(self,product_id,money):

        product=self.show_product(product_id=product_id)
        if not product:
            raise Exception("상품이 없습니다.")

        self._take_money(money=money)
        try:
            _product = self._take_out_product(product_id=product_id)
            return _product
        except Exception as e:
            self._return_money(money)
            raise e

    def _take_out_product(self,product_id):
        return self._products.pop(product_id)

    def _take_money(self, money):
        self._money+=money

    def _return_money(self,money):
        self._money-=money

            
class User:
    def __init__(self,money, store: Store):
        self._money=money
        self.store=store
        self.belongs = []

    def get_money(self):
        return self._money

    
    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_product(self,product_id):
        product = self.store.show_product(product_id=product_id)
        return product

    def purchase_product(self,product_id):
        product = self.see_product(product_id=product_id) #key word 파라미터
        price=product.price
        if self._check_money_enough(price=price):
            self._give_money(money=price)
            try:
                my_product = self.store.sell_product(product_id=product_id, money=price)
                self._add_belong(my_product)
                return my_product
            except Exception as e:
                self._take_money(money=price)
                print(f"구매중 문제가 발생했다.{str(e)}")
        else:
            raise Exception("잔돈이 부족하다")
    
    def _check_money_enough(self,price):
        return self._money>=price

    def _give_money(self,money):
        if not self._check_money_enough(price=money):
            raise Exception("돈없어용")
        self._money-=money

    def _take_money(self,money):
        self._money+=money

    def _add_belong(self,product):
        self.belongs.append(product)
            
if __name__ == "__main__":
    store = GrabStore(
        products={
            1: Product(name="키보드",price=30000),
            2: Product(name="모니터",price=50000),
        }
    )

    user = User(money=100000, store=store)
    user.purchase_product(product_id=1)
    print(f"user의 잔돈:: {user.get_money()}")
    print(f"user가 구매한 상품 : {user.get_belongs()}")