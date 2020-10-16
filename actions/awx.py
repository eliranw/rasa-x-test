import logging
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused

import json
import requests

logger = logging.getLogger(__name__)

AWX_URL_API = "http://awx.thetomcal.com/api/v2"
AWX_TOKEN = "WjUpo1QHbWRMbQRaNBEDrQITKlch1i"
AWX_USER = "admin"


class AWX:

    @staticmethod
    def get_template_survey(project_name, template_label):
        awx_templates_url = AWX_URL_API + "/job_templates?name__contains=" + project_name + "&created_by__username=" \
                            + AWX_USER + "&labels__name__contains=" + template_label
        response = requests.get(awx_templates_url, verify=False, headers={'Authorization': "Bearer " + AWX_TOKEN})
        template_id = json.loads(response.content)["results"][0]["id"]

        response = requests.get(AWX_URL_API + "/job_templates/" + str(template_id) + "/survey_spec", verify=False,
                                headers={'Authorization': "Bearer " + AWX_TOKEN})
        return json.loads(response.content)["spec"]
