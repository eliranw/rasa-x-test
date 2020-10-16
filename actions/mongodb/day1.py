import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused

import urllib
import json
import requests
from ..awx import AWX

logger = logging.getLogger(__name__)

AWX_PROJECT = "MongoDB"
AWX_LABEL = "Day%201"


class Day1(FormAction):

    def name(self) -> Text:
        return "mongodb_day1"

    @staticmethod
    def required_slots(tracker):
        print(tracker)
        questions_names = []
        for question in AWX.get_template_survey(AWX_PROJECT, AWX_LABEL):
            questions_names.append(question.variable)
        return questions_names

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],
            "size": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny", value="None"),
            ],
            "prod": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ]
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks, great job!")
        return []
