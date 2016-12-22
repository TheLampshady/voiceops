import logging
from voiceops_intent import VoiceOpsRequest


def lambda_handler(event, context={}):
    request = VoiceOpsRequest(event=event)
    return request.response()
