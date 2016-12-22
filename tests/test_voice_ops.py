from tests.base import TestBaseIntent
from src.lambda_function import lambda_handler


class TestLambda(TestBaseIntent):

    def test_lambda_creates_cloud(self):
        mock_intent = {
            "name": "CreateAWS",
        }
        mock_event = self.get_mock_event(intent=mock_intent)

        result = lambda_handler(mock_event, {})
        self.assertTrue(result)
        response = result.get("response")
        attributes = result.get("sessionAttributes")
        context = attributes.get('context')

        self.assertFalse(response.get("shouldEndSession", True), "The session ended.")
        self.assertEqual(context[0], "CreateAWS", "Context CreateAWS was not found.")

    def test_returns_current_job(self):
        mock_intent = {
            "name": "CreateAWS",
        }
        mock_event = self.get_mock_event(intent=mock_intent)
        result = lambda_handler(mock_event)

        mock_intent = {
            "name": "CurrentStatus",
        }
        mock_event = self.get_mock_event(intent=mock_intent, attributes=result['sessionAttributes'])
        result = lambda_handler(mock_event)

        attributes = result.get("sessionAttributes")
        print "ATTR", attributes
        self.assertEqual(attributes.get('context', []), ["CreateAWS"],
                         "Context CreateAWS was not found.")
