import random
from base import BaseAlexaRequest


SLOT_NAME = 'berry'


member_list = [
    "Star Wars",
    "Chewbacca",
    "Tantauns",
    "Ice Planet Hoth"
]


class MyAlexaRequest(BaseAlexaRequest):

    @property
    def GetMember(self):
        reprompt_text = None

        if self.get_slot(name=SLOT_NAME):
            value = self.get_slot(name=SLOT_NAME)
            speech_output = "I member %s. " % value
        else:
            speech_output = "I member. " \
                            "Do you member?"
            reprompt_text = "Do you member?"
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Getmember',
                response_text=speech_output,
                reprompt_text=reprompt_text
            )
        )

    @property
    def SetMember(self):
        value = self.get_slot(name=SLOT_NAME)
        if value:
            speech_output = "I love " + \
                            value + ". "
            reprompt_text = "Do you member?"
        else:
            speech_output = "Naw. " \
                            "You member?."
            reprompt_text = "Do you member?"

        self.sessionAttributes[SLOT_NAME] = value
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='SetMember',
                response_text=speech_output,
                reprompt_text=reprompt_text
            )
        )

    @property
    def LaunchRequest(self):
        response_text = "I member. " \
                        "I love " +  \
                        random.choice(member_list) + ". " \
                        "Do you Member?"
        reprompt_text = "Do you Member?"

        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Launch',
                response_text=response_text,
                reprompt_text=reprompt_text
            )
        )
