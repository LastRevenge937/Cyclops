👁️ Cyclops

Cyclops is a Python CLI app for tracking your gym lifts.
Log bench, squat, and deadlift, track PRs, see averages, and generate progress graphs — all locally, no accounts or cloud storage required.

📂 Project Structure
cyclops/
├── bench/
│   ├── tracker.py    # Script to log bench records
│   └── data.json     # Stores bench lift history
├── squat/
│   ├── tracker.py    # Script to log squat records
│   └── data.json     # Stores squat lift history
├── deadlift/
│   ├── tracker.py    # Script to log deadlift records
│   └── data.json     # Stores deadlift lift history
├── dashboard.py      # Master dashboard showing all lifts
├── run.sh            # CLI launcher for Cyclops
└── README.md         # This file

🚀 Features

Log lifts: bench, squat, deadlift

Track PRs automatically

Calculate average weight lifted

Plot progress graphs with moving averages

Master dashboard for all lifts

Fully offline, data stored in JSON

Compatible with Replit or any Python 3.9+ environment

🛠️ Requirements

Python 3.9+

matplotlib

Install dependencies:

pip install matplotlib

📥 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/cyclops.git
cd cyclops


Make the CLI executable:

chmod +x run.sh

🎮 Usage
Launch the CLI
./run.sh


Menu:

👁️ CYCLOPS
----------------
1) Add bench record
2) Add squat record
3) Add deadlift record
4) View dashboard
5) Exit


Choose 1–3 → add a new lift record

Choose 4 → generate master dashboard graph

Graphs saved as PNG (bench_progress.png, dashboard_progress.png, etc.)

JSON files store your lift history automatically

Run scripts manually (optional)
cd bench
python tracker.py

cd cyclops
python dashboard.py

📊 Graphs & Stats

Each lift generates a progress graph with moving averages

PRs are detected automatically and displayed in terminal

Dashboard shows all lifts on one graph for comparison

🔮 Future Ideas

CSV export for data analysis

Weekly averages and trends

Estimated 1RM

Date-based dashboard graphs

Add more lifts (OHP, rows, etc.)

💡 Why Cyclops?

Cyclops was built to:

Practice real Python skills

Track fitness progress offline

Keep code modular and scalable

Serve as a foundation for more advanced CLI or GUI apps

📎 Example Output

Terminal stats:

👁️ CYCLOPS — BENCH
------------------------
Sessions: 5
Average: 145.6 lbs
PR: 165 lbs
🔥 NEW PR!!! Congrats! 🔥


Saved graphs:

bench_progress.png
dashboard_progress.png

🧠 Acknowledgments

Built by a teen dev learning Python, data visualization, and CLI design.
Inspired by fitness tracking apps and open-source learning projects.

