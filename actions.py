from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted
from datetime import datetime
import datetime as dt
from datetime import timedelta
from rasa_sdk.events import AllSlotsReset

class BookingRoom(FormAction):

    def name(self) -> Text:
        return "bookingroomcall"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        print("required_slots(tracker: Tracker)")
        return ["name","roomcount","roomtype"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"name": [self.from_entity(entity="name"),
                                    self.from_text()],
                "roomcount": [self.from_entity(entity="roomcount"),
                                  self.from_text()],
                "roomtype": [self.from_entity(entity="roomtype"),
                                  self.from_text()]}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []



class CleaningTime(Action):

    def name(self) -> Text:
        return "cleaning"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

        now = dt.datetime.now()

        print(now)
        print(tracker.latest_message['text'])

        s=tracker.latest_message['text']
        result = ''.join([i for i in s if i.isdigit()])
        if result:
            result=int(result)
            print(result)
            mydate = dt.datetime.now() + timedelta(hours=result)
            finaltime = mydate.strftime("%A, %d. %B %Y %I:%M%p")
            dispatcher.utter_template("utter_info1", tracker, link=finaltime)
        elif 'right now' in result:
            dispatcher.utter_template("utter_clean_now", tracker)
        else:
            dispatcher.utter_template("utter_clean_time", tracker)
        # dispatcher.utter_message(message)
        return []


class deleteslots(Action):

    def name(self) -> Text:
        return "deleteslotss"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Deleted Slots")
        return [AllSlotsReset()]

