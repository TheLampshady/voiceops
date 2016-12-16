import unittest
from src.lambda_function import lambda_handler


class TestLambda(unittest.TestCase):

    def test_lambda_cancel_response(self):
        mock_event = {
            "session": {
                "sessionId": "SessionId.49d17730-c7b4-4ed6-8537-1a5181ceff3c",
                "application": {
                    "applicationId": "amzn1.ask.skill.bfcb8dba-c314-4433-aa04-435736c97bb8"
                },
                "attributes": {},
                "user": {
                    "userId": "amzn1.ask.account.AGWSZ4ZXDBPQRU6V7Z7Y4ZRVUTM5CQLO7MTCXT4DFNAUFWHNXZDZHD2SJIA7S6EYGDL33RJWCXYX4XW6KWKYX4LPJDGCPLLM6OCL7MRH56JMNKYJMXT26BSDGSHOWPDQE24IVCGTT7PACZXX6YBGBASZWEAXZBZSEHUIMVCCNFRH2AARKKCV72UMXNGE376HV4GBDBOTHQCZOMQ"
                },
                "new": False
            },
            "request": {
                "type": "IntentRequest",
                "requestId": "EdwRequestId.24744310-0cfc-432e-a5fd-d5f42813b8b7",
                "locale": "en-US",
                "timestamp": "2016-12-16T16:27:31Z",
                "intent": {
                    "name": "AMAZON_CancelIntent",
                    "slots": {}
                }
            },
            "version": "1.0"
        }

        result = lambda_handler(mock_event, {})
        self.assertTrue(result)
        response = result.get("response")

        self.assertTrue(response.get("shouldEndSession", False), "The session did not end.")
