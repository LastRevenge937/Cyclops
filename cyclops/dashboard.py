import json
import os
import matplotlib.pyplot as plt

lifts = ["bench", "squat", "deadlift"]
plotted = False

plt.figure(figsize=(10,6))

for lift in lifts:
    file_path = os.path.join(lift, "data.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        if data:  # only plot if there’s actual data
            weights = [entry["weight"] for entry in data]
            plt.plot(range(1, len(weights)+1), weights, marker="o", label=lift.capitalize())
            plotted = True

if plotted:
    plt.title("Cyclops — All Lifts Progress")
    plt.xlabel("Workout Number")
    plt.ylabel("Weight (lbs)")
    plt.grid(True)
    plt.legend()
    
    # Save the dashboard graph as PNG
    graph_file = "dashboard_progress.png"
    plt.savefig(graph_file)
    plt.close()
    print(f"📊 Dashboard graph saved as {graph_file}")
else:
    print("❌ No lift data found. Add some records first!")
