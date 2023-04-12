import allure
import pytest

from api.buyer.buy_now import BuyNowApi
from api.buyer.create_trade import BuyerTradeApi
from api.buyer.rog_got_goods import RogApi
from api.seller.order_seller import DeliveryApi, OrderPay


@allure.feature('疯狂购商城')
@allure.story('订单流程')
class TestOrderProcess:
    # 公共信息 order_sn
    order_sn = ''
    total_price = ''

    # 立即购买
    @allure.title('立即购买')
    def test_buy_now(self, create_goods):
        # 提取审核通过商品的 sku id
        sku_id = create_goods[1]
        print(sku_id)
        buy_now_api = BuyNowApi()
        # 将sku_id 传入立即购买接口,表示要购买该东西
        buy_now_api.params['sku_id'] = sku_id
        resp = buy_now_api.request()
        pytest.assume(resp.status_code == 200)

    # 创建交易
    @allure.title('创建交易')
    def test_create_trade(self):
        trade = BuyerTradeApi()
        resp = trade.request()
        print(resp.status_code)
        # print(resp.text)
        pytest.assume(resp.status_code == 200)
        # 提取trade_sn
        TestOrderProcess.order_sn = trade.extract_json('$.trade_sn')
        TestOrderProcess.total_price = trade.extract_json('$..total_price')
        print(TestOrderProcess.total_price)

    @allure.title('卖家发货')
    # 卖家发货  DeliveryApi
    def test_deliver(self):
        delivery = DeliveryApi(TestOrderProcess.order_sn)
        resp = delivery.request()
        print(resp.status_code)
        print(resp.text)
        pytest.assume(resp.status_code == 200)

    @allure.title('买家确认收货')
    # 买家确认收货 RogApi
    def test_rog(self):
        rogapi = RogApi(TestOrderProcess.order_sn)
        resp = rogapi.request()
        print(resp.status_code)
        print(resp.text)
        pytest.assume(resp.status_code == 200)

    # 卖家确认收款 OrderPay
    @allure.title('卖家确认收款')
    def test_order_pay(self):
        order_pay = OrderPay(TestOrderProcess.order_sn, TestOrderProcess.total_price)
        resp = order_pay.request()
        print(resp.status_code)
        # print(resp.text)
        pytest.assume(resp.status_code == 200)
