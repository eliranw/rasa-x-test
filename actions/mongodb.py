import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused
logger = logging.getLogger(__name__)


class Mongodb(Action):

    def name(self) -> Text:
        return "mongodb"

    def getActions():
        actions=[]
        # TODO AWX Call to get all templates with tag day1, day2, and info with mongodb label 
        templates = []
        for template in templates:

    def getClusters():
        actions = []
        # TODO AWX Call to get all templates with tag day1, day2, and info with mongodb label 
        clusters = []
        for template in templates:

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get name of Rocket.Chat channel so we can look for clusters in the user's namespace
        input_channel = tracker.events[1]['input_channel']

        # Feedback to user while searching for clusters
        dispatcher.utter_message(text="OK...")


        dispatcher.utter_message(text="Hey, on which one of the technologies would you like to work today? ",buttons=buttons)

        return []
