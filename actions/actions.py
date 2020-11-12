# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


courseInfo = {
    "machine learning": "74 percent of Indian business heads believe that Artificial Intelligence (AI) can augment economic growth, according to a recent PwC India report. With this growth and demand for skilled talent in mind, IEEE SIESGST has designed the one-month Certificate Program in Machine Learning & AI with Python\n- Durtion: 1 month (self placed)\n- Cost: Free\n- Faculty: Mr. X",
    "cloud computing": "Cloud Computing is the on-demand solution for storing and retrieving data globally. IEEE SIESGST Systems provides the best practice on cloud computing usage to handle big data of an organization with the remote server access with certification once course is completed!\n- Durtion: 1 month (self placed)\n- Cost: Free\n- Faculty: Mr. Y ",
    "cyber security": "This courses aims to equip students with the knowledge and skills required to defend the computer operating systems, networks and data from cyber-attacks. Any industry that transacts online or carries sensitive data is in need of a Cyber Security professional to safeguard its date from such delinquents.\n- Durtion: 1 month (self placed)\n- Cost: Free\n- Faculty: Mr. Z"
    
}


class ActionForCourseinfo(Action):

    def name(self) -> Text:
        return "action_course_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course = tracker.get_slot("courses")

        if course.lower() in courseInfo:
            dispatcher.utter_message(text=f"{courseInfo[course].capitalize()}")
            
        else:
            dispatcher.utter_message(text=f"Currently following courses are provided:\n{', '.join([i.capitalize() for i in courseInfo])}")
     
        return []



class ActionInformation(Action):
    def name(self) -> Text:
        return "action_about_ieee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        spoken = False
        for result in tracker.latest_message['entities']:
            spoken = False
            if result['entity'] == 'program_info':
                dispatcher.utter_message(text='This is the program provided by IEEE SIESGST.\nHere you will be introduced to the latest techolologies in the market, and also you will receive a certificate which you can add to your Linkdin profile.')
                spoken = True
            if result['entity'] == 'courses_info':
                #dispatcher.utter_message(text="Currently following courses are provided:")
                dispatcher.utter_message(text=f"Currently following courses are provided:\n{', '.join([i for i in courseInfo])}")
                spoken = True
        if not spoken:
            dispatcher.utter_message(text="Could you repeat what you're trying to look at?")
        return []


