from boom.pay import PayService


class TestPayService(object):

    def test_url(self):
        service = PayService()
        assert service.url == "https://pay.boom.app"
