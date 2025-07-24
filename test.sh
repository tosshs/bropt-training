# Be in repo root
cd bropt-training

# Checkout new branch
git checkout -b feature/mycroft-integration

# Create skill folder
mkdir -p mycroft-skill-bropt

# Skill init
cat <<'EOF' > mycroft-skill-bropt/__init__.py
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
EOF

# Add intents
echo "log meal {meal}" > mycroft-skill-bropt/log.meal.intent
echo "end today burned {burned} {notes}" > mycroft-skill-bropt/end.day.intent
echo "weekly summary" > mycroft-skill-bropt/weekly.summary.intent

# settingsmeta.json for Mycroft skill settings
cat <<'EOF' > mycroft-skill-bropt/settingsmeta.json
{
  "name": "BroPT Skill",
  "skillMetadata": {
    "sections": [
      {
        "name": "OpenAI Settings",
        "fields": [
          {
            "type": "text",
            "label": "OpenAI API Key",
            "name": "openai_api_key"
          }
        ]
      }
    ]
  }
}
EOF

# Update README
echo -e "\n## 🎙️ Mycroft Voice Mode\n\nNow you can talk to BroPT via Mycroft!\n\n- Say: *Hey BroPT, log meal 200g chicken breast and 100g rice*\n- Say: *Hey BroPT, end today burned 2200 push day*\n- Say: *Hey BroPT, weekly summary*\n\nIt calls ChatGPT API and still logs food into logs/food_log.jsonl.\n" >> README.md

# Commit & push
git add .
git commit -m "🎙️ Mycroft Integration: Voice-controlled savage food logging + BroPT replies"
git push origin feature/mycroft-integration

# Open PR (requires GitHub CLI)
gh pr create --title "🎙️ Mycroft Integration: Voice-controlled savage food logging + BroPT replies" --body "Adds Mycroft Skill for voice-based BroPT macro logging + savage responses." --base main --head feature/mycroft-integration

