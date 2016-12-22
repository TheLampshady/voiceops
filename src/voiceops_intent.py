import random
from base import BaseAlexaRequest

context_translations = {
    "CreateAWS": "Creating Amazon Web Service.",
    "CreateGCE": "Creating Google Cloud Engine.",
}

help_list = [
    "Create a Cloud instance with A.W.S or G.C.E",
    "Command your Jenkins",
    "Create a web service",
    "Load test site"
]

prompt_selection = [
    "I am assuming Stan is busy",
    "You must be truly desperate to come here.",
    "What do you need?",
    "You can't just press a button to make it work. Oh wait that's what I'm for.",
    "Will deploy for additional resources."
]

help_text = [
    "Don't be shy to ask for help.",
    "Sounds like someone needs help..."
]


SIZE_PROMT = "Please select a small, medium or large instance."


class VoiceOpsRequest(BaseAlexaRequest):

    def CreateAWS(self):
        self.add_context("CreateAWS")
        speech_output = "Ahh yes Amazon. Large, Medium or small instance."
        reprompt_text = SIZE_PROMT
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Creating an AWS Instance',
                response_text=speech_output,
                reprompt_text=reprompt_text
            )
        )

    def CreateGCE(self):
        self.add_context("CreateGCE")
        speech_output = "Ahh yes Google. Large, Medium or small instance."
        reprompt_text = SIZE_PROMT

        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Creating a GCE Instance',
                response_text=speech_output,
                reprompt_text=reprompt_text
            )
        )

    def CurrentStatus(self):
        job = context_translations.get(self.current_context)
        if job:
            speech_output = "You are working on the {j}.".format(j=job)
            reprompt_text = "Continue {j}?".format(j=job)
        else:
            speech_output = "There is no current job. Feel free to start one."
            reprompt_text = random.choice(prompt_selection)
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='You Member',
                response_text=speech_output,
                reprompt_text=reprompt_text
            )
        )

    def LaunchRequest(self):
        response_text = "Welcome to Voice Ops. How may I help you?"
        reprompt_text = random.choice(prompt_selection)

        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Launch',
                response_text=response_text,
                reprompt_text=reprompt_text
            )
        )

    def AMAZON_HelpIntent(self):
        return self.build_response(
            speechletResponse=self.build_speechlet_response(
                title='Help Intent',
                response_text="Well, you got a couple of options." + ", ".join(help_list),
                reprompt_text="Say 'help' to repeat the options."
            )
        )

    def AMAZON_StopIntent(self):
        super(VoiceOpsRequest, self).AMAZON_StopIntent()
