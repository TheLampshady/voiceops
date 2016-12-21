import logging


class BaseAlexaRequest(object):

    @property
    def intent(self):
        return self.event['request']['intent']

    @property
    def intent_name(self):
        return self.event['request']['intent']['name']

    @property
    def request_type(self):
        return self.event['request']['type']

    def __init__(self, event):
        self.event = event
        session = event.get("session", {})
        self.sessionAttributes = session.get("attributes", {})

    def build_response(self, speechletResponse):
        return dict(
            version='1.0',
            sessionAttributes=self.sessionAttributes,
            response=speechletResponse,
        )

    def build_speechlet_response(self, title, response_text, reprompt_text=None):
        output = dict(
            outputSpeech=dict(
                type='PlainText',
                text=response_text,
            ),
            card=dict(
                type='Simple',
                title=title,
                content=response_text,
            ),
            shouldEndSession=True,
        )
        if reprompt_text is not None:
            output['reprompt'] = dict(
                outputSpeech=dict(
                    type='PlainText',
                    text=reprompt_text,
                )
            )
            output['shouldEndSession'] = False
        return output

    def get_slot(self, name):
        try:
            return self.intent['slots'][name]['value']
        except KeyError as ae:
            logging.warning("No Session Attribute ")
            return None

    def response(self):
        if self.request_type == 'IntentRequest':
            intent_name = self.intent_name.replace('.', '_')
            try:
                return getattr(self, intent_name)
            except AttributeError as ae:
                logging.info("Intent Not Implemented: %s" % intent_name)
                raise ae
        elif self.request_type == "LaunchRequest":
            return self.LaunchRequest
        return 'intentType: {s.request_type}'.format(s=self)

    @property
    def AMAZON_CancelIntent(self):
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='CancelIntent',
                response_text='goodbye',
            )
        )

    @property
    def AMAZON_StopIntent(self):
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Stop Intent',
                response_text='goodbye',
            )
        )

    @property
    def AMAZON_HelpIntent(self):
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Help Intent',
                response_text="You don't need help to member",
                reprompt_text="Try to member."
            )
        )