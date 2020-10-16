import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused

logger = logging.getLogger(__name__)


class TechnologiesForm(FormAction):

    # The name function is required every time you create a form.
    def name(self):
        return "techonology_form"

    # Like the name function, the required_slots function is required too. As the name suggests, it configures which
    # slots are required by the form. In addition to specifying the required slots, we’re also introducing a bit of
    # conditional logic.
    @staticmethod
    def required_slots(tracker):
        mongo_create_path = ["technology", "options", "create_mongo_cluster"]
        postgres_create_path = ["technology", "options", "create_postgres_cluster"]
        if tracker.get_slot('technology') == "postgres":
            return postgres_create_path
        else:
            return mongo_create_path

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "confirm_exercise": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny", value="None"),
            ],
            "diet": [
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny"),
            ],
            "goal": [
                self.from_text(intent="inform"),
            ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []
