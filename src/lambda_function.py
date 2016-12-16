from my_intent import MyAlexaRequest


def lambda_handler(event, context):
    return MyAlexaRequest(event=event).response()
