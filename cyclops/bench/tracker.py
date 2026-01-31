import json
import os
import matplotlib.pyplot as plt
from datetime import date

# --------- Detect lift ----------
LIFT_NAME = os.path.basename(os.getcwd())
DATA_FILE = "data.json"

# --------- Load data ----------
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        weights = json.load(f)
else:
    weights = []

# --------- Input ----------
today_weight = int(input(f"Enter today's {LIFT_NAME} weight (lbs): "))
today_date = str(date.today())
weights.append({"date": today_date, "weight": today_weight})

# --------- Save data ----------
with open(DATA_FILE, "w") as f:
    json.dump(weights, f)

# --------- Stats ----------
all_weights = [entry["weight"] for entry in weights]
average = sum(all_weights) / len(all_weights)
pr = max(all_weights)

print(f"\n👁️ CYCLOPS — {LIFT_NAME.upper()}")
print("------------------------")
print(f"Sessions: {len(weights)}")
print(f"Average: {average:.1f} lbs")
print(f"PR: {pr} lbs")
if today_weight == pr:
    print("🔥 NEW PR!!! Congrats! 🔥")

# --------- Moving Average ----------
def moving_average(data, n=3):
    if len(data) < n:
        return data
    return [sum(data[i-n:i])/n for i in range(n, len(data)+1)]

ma = moving_average(all_weights)

# --------- Graph ----------
plt.plot(range(1, len(all_weights)+1), all_weights, marker="o", label="Raw")
plt.plot(range(len(all_weights)-len(ma)+1, len(all_weights)+1), ma, marker="x", label="Moving Avg")
plt.title(f"{LIFT_NAME.capitalize()} Progress")
plt.xlabel("Workout Number")
plt.ylabel("Weight (lbs)")
plt.grid(True)
plt.legend()
plt.show()
