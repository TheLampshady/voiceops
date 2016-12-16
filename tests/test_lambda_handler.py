import unittest
from src.lambda_function import lambda_handler


class TestLambda(unittest.TestCase):

    def get_mock_event(self, intent, session_id="SessionId.uuid"):
        return {
            "session": {
                "sessionId": session_id,
                "application": {
                    "applicationId": "amzn1.ask.skill.1234"
                },
                "attributes": {},
                "user": {
                    "userId": "user_id"
                },
                "new": False
            },
            "request": {
                "type": "IntentRequest",
                "requestId": "EdwRequestId.24744310-0cfc-432e-a5fd-d5f42813b8b7",
                "locale": "en-US",
                "timestamp": "2016-12-16T16:27:31Z",
                "intent": intent
            },
            "version": "1.0"
        }

    def test_lambda_cancel_response(self):
        mock_intent = {
                    "name": "AMAZON_CancelIntent",
                    "slots": {}
                }
        mock_event = self.get_mock_event(intent=mock_intent)

        result = lambda_handler(mock_event, {})
        self.assertTrue(result)
        response = result.get("response")

        self.assertTrue(response.get("shouldEndSession", False), "The session did not end.")

    def test_lambda_sets_color(self):
        mock_intent = {
            "name": "MyColorIsIntent",
            "slots": {
                "Color": {
                      "name": "Color",
                      "value": "red"
                }
            }
        }
        mock_event = self.get_mock_event(intent=mock_intent)

        result = lambda_handler(mock_event, {})
        self.assertTrue(result)
        response = result.get("response")
        attributes = result.get("sessionAttributes")

        self.assertFalse(response.get("shouldEndSession", True), "The session ended.")
        self.assertEqual(attributes.get("favoriteColor", ""), "red", "The color was not saved.")
