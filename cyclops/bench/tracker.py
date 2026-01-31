import json
import os
import matplotlib.pyplot as plt
from datetime import date

# Detect lift name from folder
LIFT_NAME = os.path.basename(os.getcwd())
DATA_FILE = "data.json"

# Load existing data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        weights = json.load(f)
else:
    weights = []

# Input today's weight
today_weight = int(input(f"Enter today's {LIFT_NAME} weight (lbs): "))
today_date = str(date.today())
weights.append({"date": today_date, "weight": today_weight})

# Save updated data
with open(DATA_FILE, "w") as f:
    json.dump(weights, f)

# Stats
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

# Moving Average function
def moving_average(data, n=3):
    if len(data) < n:
        return data
    return [sum(data[i-n:i])/n for i in range(n, len(data)+1)]

ma = moving_average(all_weights)

# Plot graph and save it
plt.figure(figsize=(8,5))
plt.plot(range(1, len(all_weights)+1), all_weights, marker="o", label="Raw")
plt.plot(range(len(all_weights)-len(ma)+1, len(all_weights)+1), ma, marker="x", label="Moving Avg")
plt.title(f"{LIFT_NAME.capitalize()} Progress")
plt.xlabel("Workout Number")
plt.ylabel("Weight (lbs)")
plt.grid(True)
plt.legend()

# Save as PNG instead of showing
graph_file = f"{LIFT_NAME}_progress.png"
plt.savefig(graph_file)
plt.close()  # closes the figure
print(f"📊 Graph saved as {graph_file}")
