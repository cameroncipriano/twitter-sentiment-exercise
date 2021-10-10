# import GoogleNLP Library
from google.cloud import language_v1
from google.api_core.exceptions import InvalidArgument


class GoogleNLP:
    def __init__(self) -> None:
        self._client = language_v1.LanguageServiceClient()
        self._type = language_v1.Document.Type.PLAIN_TEXT

    def get_sentiment(self, text_to_analyze):
        document = {
            "content": text_to_analyze,
            "type_": self._type,
        }

        try:
            sentiment = self._client.analyze_sentiment(request={
                "document": document
            }).document_sentiment
        except InvalidArgument:
            return 0.0

        return sentiment.score
