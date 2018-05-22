from boom.order import OrderService


class TestOrderService(object):

    def test_url(self):
        service = OrderService()
        assert service.url == "https://order.boom.app"
