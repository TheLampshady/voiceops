import random
from base import BaseAlexaRequest


SLOT_NAME = 'berry'


member_list = [
    "Star Wars",
    "Chew Bacca",
    "Tawn Tawns",
    "Ice Planet Hoth",
    "Han Solo"
]

member_response = [
    "I member {b}",
    "Oh yes, {b}. I member",
    "Oooo {b}, yes!",
    "I love {b}! I member {b}"
]


class MemberRequest(BaseAlexaRequest):

    @property
    def GetMember(self):
        reprompt_text = None

        if self.get_slot(name=SLOT_NAME):
            value = self.get_slot(name=SLOT_NAME)
            speech_output = random.choice(member_response).format(b=value)
        else:
            speech_output = "I member. Do you member?"
            reprompt_text = "Do you member?"
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='I Member',
                response_text=speech_output,
                reprompt_text=reprompt_text
            )
        )

    @property
    def SetMember(self):
        value = self.get_slot(name=SLOT_NAME)
        if value:
            speech_output = random.choice(member_response).format(b=value)
            reprompt_text = "Do you member?"
        else:
            speech_output = "Naw. You member?."
            reprompt_text = "Do you member?"

        self.sessionAttributes[SLOT_NAME] = value
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='You Member',
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

    @property
    def AMAZON_HelpIntent(self):
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Help Intent',
                response_text="You don't need help to member",
                reprompt_text="Try to member."
            )
        )