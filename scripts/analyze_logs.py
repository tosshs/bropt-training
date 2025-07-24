#!/usr/bin/env python3
import json, os, statistics

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "logs", "food_log.jsonl")

def analyze_week():
    if not os.path.exists(LOG_FILE):
        print("No logs yet, bro. Start tracking before asking for stats.")
        return

    logs = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            logs.append(json.loads(line))

    if not logs:
        print("Empty log file. Stop slacking.")
        return

    week = logs[-7:]
    cals_in = [entry["cals_in"] for entry in week]
    cals_burned = [entry["cals_burned"] for entry in week]
    deficits = [entry["deficit"] for entry in week]
    protein = [entry["protein_g"] for entry in week]

    print("📊 Weekly Recap:")
    print(f"- Avg Intake: {statistics.mean(cals_in):.0f} kcal")
    print(f"- Avg Burn:   {statistics.mean(cals_burned):.0f} kcal")
    print(f"- Avg Deficit: {statistics.mean(deficits):+.0f} kcal")
    print(f"- Protein Avg: {statistics.mean(protein):.0f} g")

    if statistics.mean(protein) < 120:
        print("Bro: Protein’s weak. Eat more meat, tofu, SOMETHING.")
    if statistics.mean(deficits) > 0:
        print("Bro: You’re gaining, not losing. Admit the bulk.")
    elif statistics.mean(deficits) < -500:
        print("Bro: Starving yourself won’t make you shredded overnight.")

if __name__ == "__main__":
    analyze_week()
