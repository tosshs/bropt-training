#!/usr/bin/env python3
import json, os, sys
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "logs", "food_log.jsonl")
FOOD_DB = os.path.join(os.path.dirname(__file__), "..", "data", "food_macros.json")

# Load food macro DB
with open(FOOD_DB, "r") as f:
    FOOD_MACROS = json.load(f)

# Track running totals
TODAY_TOTALS = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0, "meals": []}

def log_meal(meal_desc):
    parts = meal_desc.lower().split(",")
    meal_cals, meal_protein, meal_carbs, meal_fats = 0, 0, 0, 0
    meal_details = []
    for part in parts:
        part = part.strip()
        # Expect like "200g chicken breast"
        qty, food = part.split(" ", 1)
        qty_g = float(qty.replace("g",""))
        if food in FOOD_MACROS:
            ref = FOOD_MACROS[food]
            ratio = qty_g / 100.0
            meal_cals += ref["calories"] * ratio
            meal_protein += ref["protein"] * ratio
            meal_carbs += ref["carbs"] * ratio
            meal_fats += ref["fats"] * ratio
            meal_details.append(f"{qty_g}g {food}")
        else:
            print(f"Bro: I don’t know '{food}'. Add it to the DB.")
    # Update running totals
    TODAY_TOTALS["calories"] += meal_cals
    TODAY_TOTALS["protein"] += meal_protein
    TODAY_TOTALS["carbs"] += meal_carbs
    TODAY_TOTALS["fats"] += meal_fats
    TODAY_TOTALS["meals"].append(meal_details)

    # Print meal summary
    print(f"Meal → ~{meal_cals:.0f} kcal | 🥩 {meal_protein:.1f}g | 🍞 {meal_carbs:.1f}g | 🧈 {meal_fats:.1f}g")
    if meal_protein < 20:
        print("Bro: Weak protein hit. Try harder.")
    elif meal_cals > 800:
        print("Bro: Big meal. You bulking or just hungry?")

def end_of_day(cals_burned, notes=""):
    date = datetime.now().strftime("%d.%m.%Y")
    deficit = TODAY_TOTALS["calories"] - cals_burned
    entry = {
        "date": date,
        "cals_in": round(TODAY_TOTALS["calories"],1),
        "cals_burned": cals_burned,
        "deficit": deficit,
        "protein_g": round(TODAY_TOTALS["protein"],1),
        "carbs_g": round(TODAY_TOTALS["carbs"],1),
        "fats_g": round(TODAY_TOTALS["fats"],1),
        "notes": notes
    }
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"📅 {date} | 🍽️ {entry['cals_in']} kcal | 🔥 {cals_burned} kcal | "
          f"{deficit:+} kcal | 🥩 {entry['protein_g']}g | 🍞 {entry['carbs_g']}g | 🧈 {entry['fats_g']}g | 🏋️‍♂️ {notes}")
    if entry['protein_g'] < 120:
        print("Bro: Low protein. Enjoy losing gains.")
    if deficit > 0:
        print("Bro: Surplus. Bulking stealth mode? Admit it.")
    elif deficit < -500:
        print("Bro: Hardcore cut. Don’t cry later.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  log_food.py meal '200g chicken breast, 100g rice cooked, 10g olive oil'")
        print("  log_food.py end <cals_burned> <notes>")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "meal":
        meal_desc = " ".join(sys.argv[2:])
        log_meal(meal_desc)
    elif mode == "end":
        cals_burned = float(sys.argv[2])
        notes = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
        end_of_day(cals_burned, notes)
