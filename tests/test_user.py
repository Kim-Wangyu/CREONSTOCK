
import pytest


def test_check_money(user):
    cheap_price = 500
    expensive_price = 1000000

    can_buy= user._check_money_enough(price=cheap_price)  #하나의 체크에서 하나만 하기 단일책임원칙
    assert can_buy

    can_buy= user._check_money_enough(price=expensive_price)
    assert not can_buy

def test_give_money_cheaper(user):
    price = 500

    pre_money = user._money


def test_give_money_expensive(user):
    price=1000000


    with pytest.raises(Exception):
        user._give_money(money=price)





   