from base import BaseAlexaRequest


class MyAlexaRequest(BaseAlexaRequest):

    @property
    def WhatsMyColorIntent(self):
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='HowAreYou',
                response_text='i am fine thanks',
            )
        )

    @property
    def MyColorIsIntent(self):
        name = self.get_slot(name='myName')
        self.sessionAttributes['myName'] = name
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='MyNameIsIntent',
                response_text='your name is {name}'.format(name=name)
            )
        )

    @property
    def StateRequestIntent(self):
        state = self.get_slot(name='usstate')
        states = self.sessionAttributes.get('states', None)
        if states is None:
            self.sessionAttributes['states'] = [state]
        elif state not in states:
            self.sessionAttributes['states'].append(state)

        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='StateRequestIntent',
                response_text='you picked {state}'.format(state=self.get_slot(name='usstate'))
            )
        )
