#!/bin/bash

echo "👁️ Welcome to Cyclops!"
echo "1) Add new lift record"
echo "2) View dashboard"
read -p "Choose 1 or 2: " choice

if [ "$choice" == "1" ]; then
    echo "Which lift? (bench/squat/deadlift)"
    read lift
    if [ -f "$lift/tracker.py" ]; then
        python "$lift/tracker.py"
    else
        echo "❌ That lift doesn't exist!"
    fi
elif [ "$choice" == "2" ]; then
    if [ -f "dashboard.py" ]; then
        python dashboard.py
    else
        echo "❌ Dashboard not found!"
    fi
else
    echo "❌ Invalid choice!"
fi
