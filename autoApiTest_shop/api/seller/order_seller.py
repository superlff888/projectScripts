from api.seller.base_seller import BaseSellerApi


class DeliveryApi(BaseSellerApi):
    """卖家发货"""

    def __init__(self, order_sn):
        """/seller/trade/orders/20221120000087/delivery"""

        super().__init__()
        # 交易单号 动态数据
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/delivery'
        self.method = 'post'
        self.data = {'ship_no': '001', 'logi_id': 13, 'logi_name': '中通01'}


class OrderPay(BaseSellerApi):
    """卖家确认收款"""

    # 商品价格 动态传参
    def __init__(self, order_sn, pay_price):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/pay'
        self.method = 'post'
        self.data = {'pay_price': pay_price}
        self.desc = '卖家确认收款'