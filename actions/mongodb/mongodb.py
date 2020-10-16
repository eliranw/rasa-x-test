import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused
import random as rand

logger = logging.getLogger(__name__)

# TODO get name of tech from the inherited class

OPTIONS = [{"button_text": "Create new mongodb cluster",
            "intent": "day1",
            "clusters_exist": False},
           {"button_text": "Manage an existing mongodb cluster",
            "intent": "day2",
            "clusters_exist": True},
           {"button_text": "Get info about an existing mongodb cluster",
            "intent": "info",
            "clusters_exist": True}
           ]


class Mongodb(Action):

    def name(self) -> Text:
        return "mongodb"

    def get_actions(self):
        actions = []
        # TODO AWX Call to get all templates with tag day1, day2, and info with mongodb label 
        templates = []
        for template in templates:
            pass

    # Get all clusters names from a namespace in openshift
    def get_clusters(self, namespace):
        actions = []
        # TODO AWX Call to get all templates with tag day1, day2, and info with mongodb label 
        clusters = []
        return clusters

    # Send back all the options the user can do in the current namespace of his channel: day1, day2, info
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get name of Rocket.Chat channel so we can look for clusters in the user's namespace
        input_channel = tracker.events[1]['input_channel']

        # Feedback to user while searching for clusters
        dispatcher.utter_message(text="Getting all your clusters, be right back :)")

        clusters_exist = bool(len(self.get_clusters()))

        buttons = []
        for option in OPTIONS:
            if option["clusters_exist"]:
                if clusters_exist:
                    buttons.append({"title": option["button_text"], "payload": option["intent"] + "_" + self.name()})
            else:
                buttons.append({"title": option["button_text"], "payload": option["intent"] + "_" + self.name()})

        dispatcher.utter_message(text="I'm back homie, what would you like to do? ",
                                 buttons=buttons)
        return []
