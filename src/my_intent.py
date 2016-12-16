from base import BaseAlexaRequest


class MyAlexaRequest(BaseAlexaRequest):

    @property
    def WhatsMyColorIntent(self):
        reprompt_text = None

        if self.get_slot(name='favoriteColor'):
            favorite_color = self.get_slot(name='favoriteColor')
            speech_output = "Your favorite color is " + favorite_color + \
                            ". Goodbye."
        else:
            speech_output = "I'm not sure what your favorite color is. " \
                            "You can say, my favorite color is red."
            reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='HowAreYou',
                response_text=speech_output,
                reprompt_text=reprompt_text
            )
        )

    @property
    def MyColorIsIntent(self):
        favorite_color = self.get_slot(name='Color')
        if favorite_color:
            speech_output = "I now know your favorite color is " + \
                            favorite_color + \
                            ". You can ask me your favorite color by saying, " \
                            "what's my favorite color?"
            reprompt_text = "You can ask me your favorite color by saying, " \
                            "what's my favorite color?"
        else:
            speech_output = "I'm not sure what your favorite color is. " \
                            "Please try again."
            reprompt_text = "I'm not sure what your favorite color is. " \
                            "You can tell me your favorite color by saying, " \
                            "my favorite color is red."

        self.sessionAttributes['favoriteColor'] = favorite_color
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='MyColorIsIntent',
                response_text=speech_output,
                reprompt_text=reprompt_text
            )
        )

    @property
    def LaunchRequest(self):
        response_text = "Welcome to the Alexa Skills Kit sample. " \
                        "Please tell me your favorite color by saying, " \
                        "my favorite color is red"
        reprompt_text = "Please tell me your favorite color by saying, " \
                        "my favorite color is red."

        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Welcome',
                response_text=response_text,
                reprompt_text=reprompt_text
            )
        )
