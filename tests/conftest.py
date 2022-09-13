
import pytest

from allinrefacto import GrabStore, Product, User


@pytest.fixture(scope="function") # scope = 테스트함수에서 불러올 때 계속 불릴것이냐 아니면 기존의 한번만 올것인가, pytest fixture의 기본 scope는 function입니다.
def grab_store():
    return GrabStore(
            products={
                1: Product(name="키보드",price=30000),
                2: Product(name="모니터",price=50000),
            }
    )

@pytest.fixture(scope="function")
def user(grab_store):
    return User(money=100000,store=grab_store)