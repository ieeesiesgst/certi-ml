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

subchapters = {
    "wie": "IEEE WIE is one of the world’s leaders in changing the face of engineering. Our global network connects nearly 20,000 members in over 100 countries to advance women in technology at all points in their life and career. IEEE WIE members make lifelong friendships, acquire influential mentors, and make a difference for the benefit of humanity.",
    "women in engineering": "IEEE WIE is one of the world’s leaders in changing the face of engineering. Our global network connects nearly 20,000 members in over 100 countries to advance women in technology at all points in their life and career. IEEE WIE members make lifelong friendships, acquire influential mentors, and make a difference for the benefit of humanity.",
    "microwave theory and techniques society": "The IEEE Microwave Theory and Techniques Society (MTT-S) is a transnational society with more than 10,500 members and 190 chapters worldwide. Our society promotes the advancement of microwave theory and its applications, including RF, microwave, millimeter-wave, and terahertz technologies.",
    "mtts": "The IEEE Microwave Theory and Techniques Society (MTT-S) is a transnational society with more than 10,500 members and 190 chapters worldwide. Our society promotes the advancement of microwave theory and its applications, including RF, microwave, millimeter-wave, and terahertz technologies.",
    "computer society":"IEEE Computer Society is a professional society of the Institute of Electrical and Electronics Engineers. Its purpose and scope is 'to advance the theory, practice, and application of computer and information processing science and technology' and the 'professional standing of its members.'",
    "cs":"IEEE Computer Society is a professional society of the Institute of Electrical and Electronics Engineers. Its purpose and scope is 'to advance the theory, practice, and application of computer and information processing science and technology' and the 'professional standing of its members.'"

}

sociallinks = {
    "linkedin": "Click [here](https://www.linkedin.com/company/ieee-gst/) to visit our LinkedIn Page.",
    "instagram": "Click [here](https://www.instagram.com/ieeesiesgst/) to visit our Instagram Page.",
    "insta": "Click [here](https://www.instagram.com/ieeesiesgst/) to visit our Instagram Page.",
    "facebook": "Click [here](https://www.facebook.com/ieeesiesgstofficial/) to visit our Facebook Page.",
    "fb": "Click [here](https://www.facebook.com/ieeesiesgstofficial/) to visit our Facebook Page.",
    "youtube": "Click [here](https://www.youtube.com/channel/UCXAeBcDQQBiuVtzn4ke-Xsw) to visit our YouTube channel.",
}


class ActionForCourseinfo(Action):

    def name(self) -> Text:
        return "action_course_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = tracker.get_slot("courses")
        if course.lower() in courseInfo:
            dispatcher.utter_message(text=f"{courseInfo[course.lower()].capitalize()}")    
        else:
            dispatcher.utter_message(text=f"Currently following courses are provided:\n{', '.join([i.capitalize() for i in courseInfo])} \nTo get more details, let me know in which course you are interested..!")
        return []



class ActionAboutIeee(Action):
    def name(self) -> Text:
        return "action_about_ieee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        spoken = False
        subchap = tracker.get_slot("sub_chapters")
        for result in tracker.latest_message['entities']:
            if result['entity'] == 'ieee':
                dispatcher.utter_message(template='utter_about_ieee')
                spoken = True
            if result['entity'] == 'sub_chapters':
                if subchap.lower() in subchapters:
                    dispatcher.utter_message(text=f"{subchapters[subchap.lower()]}")
                else:
                    dispatcher.utter_message(text="IEEE SIESGST has 3 sub-chapters:\n- WIE(Women In Engineering)\n- MTTS(Microwave Theory and Techniques Society)\n- CS(Computer Society)")
                spoken = True
        if not spoken:
            dispatcher.utter_message(text="Could you repeat what you're trying to look at?")
        return []



class ActionContactInfo(Action):
    def name(self) -> Text:
        return "action_contact_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        spoken = False
        social = tracker.get_slot("social_links")
        for result in tracker.latest_message['entities']:
            if result['entity'] == 'contact':
                dispatcher.utter_message(text="Following are our active social media handles: \n1) [LinkedIn](https://www.linkedin.com/company/ieee-gst/)\n2) [Youtube](https://www.youtube.com/channel/UCXAeBcDQQBiuVtzn4ke-Xsw)\n3) [Instagram](https://www.instagram.com/ieeesiesgst/)\n4) [Facebook](https://www.facebook.com/ieeesiesgstofficial/). \nFor more info [Contact Us](https://ieeesiesgst.co.in/contact.html)")
                spoken = True
            if result['entity'] == 'social_links':
                if social.lower() in sociallinks:
                    dispatcher.utter_message(text=f"{sociallinks[social.lower()]}")
                else:
                    dispatcher.utter_message(text="Following are our active social media handles: \n1) LinkedIn \n2) Youtube \n3) Instagram \n4) Facebook.")
                    dispatcher.utter_message(text="I can also provide you the the links of any specified social media handles if you want! :D")
                spoken = True
        if not spoken:
            dispatcher.utter_message(text="Could you repeat what you're trying to look at?")
        return []