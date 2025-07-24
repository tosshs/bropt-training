#!/usr/bin/env python3
import json, os, sys
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "logs", "food_log.jsonl")

def log_food_entry(cals_in, cals_burned, protein, carbs, fats, notes=""):
    date = datetime.now().strftime("%d.%m.%Y")
    deficit = cals_in - cals_burned
    entry = {
        "date": date,
        "cals_in": cals_in,
        "cals_burned": cals_burned,
        "deficit": deficit,
        "protein_g": protein,
        "carbs_g": carbs,
        "fats_g": fats,
        "notes": notes
    }
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

    verdict = "deficit" if deficit < 0 else "surplus"
    print(f"📅 {date} | 🍽️ {cals_in} kcal | 🔥 {cals_burned} kcal | "
          f"{deficit:+} kcal | 🥩 {protein}g | 🍞 {carbs}g | 🧈 {fats}g | 🏋️‍♂️ {notes}")

    if protein < 100:
        print("Bro: Protein that low? You tryna stay skinny?")
    elif deficit < -300:
        print("Bro: Cutting HARD. Respect… but don’t cry about it later.")
    elif deficit > 0:
        print("Bro: Bulking… or just lazy with your cardio?")

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("Usage: log_food.py <cals_in> <cals_burned> <protein_g> <carbs_g> <fats_g> <notes>")
        sys.exit(1)
    cals_in = float(sys.argv[1])
    cals_burned = float(sys.argv[2])
    protein = float(sys.argv[3])
    carbs = float(sys.argv[4])
    fats = float(sys.argv[5])
    notes = " ".join(sys.argv[6:])
    log_food_entry(cals_in, cals_burned, protein, carbs, fats, notes)
