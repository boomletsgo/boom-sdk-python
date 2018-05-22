from boom.conversation import ConversationService


class TestConversationService(object):

    def test_url(self):
        service = ConversationService()
        assert service.url == "https://conversation.boom.app"
