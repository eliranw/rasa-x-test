import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused

logger = logging.getLogger(__name__)

TECHNOLOGIES_LIST = ["Postgres", "MongoDB"]


class Technologies(Action):

    def name(self) -> Text:
        return "technologies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        answer_str = "Hey, what technology would you like to use today?"
        buttons = []
        for tech in TECHNOLOGIES_LIST:
            buttons.append({"title": tech, "payload": tech})

        dispatcher.utter_message(text="Hey, on which one of the technologies would you like to work today? ",
                                 buttons=buttons)

        return []
