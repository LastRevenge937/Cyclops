import json
import os
import matplotlib.pyplot as plt

lifts = ["bench", "squat", "deadlift"]
plotted = False

for lift in lifts:
    file_path = os.path.join(lift, "data.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        if data:
            weights = [entry["weight"] for entry in data]
            plt.plot(weights, marker="o", label=lift.capitalize())
            plotted = True

if plotted:
    plt.title("Cyclops — All Lifts Progress")
    plt.xlabel("Workout Number")
    plt.ylabel("Weight (lbs)")
    plt.grid(True)
    plt.legend()
    plt.savefig("dashboard.png")
    print("📊 Dashboard saved as dashboard.png")
else:
    print("❌ No lift data found. Add some records first!")

