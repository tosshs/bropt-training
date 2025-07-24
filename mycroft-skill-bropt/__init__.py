from mycroft import MycroftSkill, intent_handler
import openai, json, os

class BroptSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.log_file = os.path.join(os.path.dirname(__file__), "..", "logs", "food_log.jsonl")

    def bropt_request(self, user_text):
        openai.api_key = self.api_key
        resp = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are BroPT, a savage bro with dual modes: roast + macro tracker."},
                {"role": "user", "content": user_text}
            ]
        )
        return resp.choices[0].message["content"]

    @intent_handler('log.meal.intent')
    def handle_log_meal(self, message):
        meal = message.data.get('meal')
        response = self.bropt_request(f"Log this meal: {meal}")
        self.speak(response)
        with open(self.log_file, "a") as f:
            f.write(json.dumps({"meal": meal, "response": response}) + "\n")

    @intent_handler('end.day.intent')
    def handle_end_day(self, message):
        burned = message.data.get('burned')
        notes = message.data.get('notes') or ""
        response = self.bropt_request(f"End today, burned {burned} kcal, notes: {notes}")
        self.speak(response)

    @intent_handler('weekly.summary.intent')
    def handle_weekly_summary(self, message):
        response = self.bropt_request("Give me weekly macro summary")
        self.speak(response)

def create_skill():
    return BroptSkill()
