from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Import the getData module to fetch the data.
from dbConnect import getData


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # write the sql query here.
        query = "select * from customer"

        # pass the sql query to the getData method and store the results in `data` variable.
        data = getData(query)

        print("data: ", data)

        dispatcher.utter_message(text="Hello World!", json_message=data)

        return []
