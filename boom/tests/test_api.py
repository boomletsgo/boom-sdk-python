from boom.api import API


class TestAPI(object):

    def test_links(self):
        api = API()
        urls = api.urls
        assert "index" in urls
        assert "client" in urls
        assert "client-location" in urls
        assert "client-location-experience" in urls
        assert "client-location-platform" in urls
        assert "experience" in urls
        assert "platform" in urls
        assert "conversation" in urls
        assert "message" in urls

    def test_headers(self):
        api = API()
        headers = api.get_headers()
        assert headers == {"Content-Type": "application/json"}

    def test_make_url(self):
        api = API()
        url = api.make_url("test")
        assert url == "https://api.boomletsgo.com/test"

    def test_make_url_with_leading_slash(self):
        api = API()
        url = api.make_url("/test")
        assert url == "https://api.boomletsgo.com/test"

    def test_make_url_with_querystring(self):
        api = API()
        url = api.make_url("test", {"option": "on"})
        assert url == "https://api.boomletsgo.com/test?option=on"

    def test_generate_endpoint_url(self):
        api = API()
        url = api.generate_endpoint_url("index")
        assert url == "https://api.boomletsgo.com/"

    def test_generate_endpoint_url_with_tokens(self):
        api = API()
        url = api.generate_endpoint_url("client", client_id="308a12ce-570e-4837-a374-f69d26713aa8")
        assert url == "https://api.boomletsgo.com/client/308a12ce-570e-4837-a374-f69d26713aa8"

    def test_generate_endpoint_url_with_querystring(self):
        api = API()
        url = api.generate_endpoint_url("client", option="on")
        assert url == "https://api.boomletsgo.com/client?option=on"

    def test_generate_endpoint_url_with_data(self):
        api = API()
        url = api.generate_endpoint_url("client", {"client_id": "308a12ce-570e-4837-a374-f69d26713aa8"})
        assert url == "https://api.boomletsgo.com/client/308a12ce-570e-4837-a374-f69d26713aa8"

    def test_normalize_data(self):
        api = API()
        data = {"anything": "goes"}
        dataset = api.normalize_data(data)

        assert dataset == [{"anything": "goes"}]
