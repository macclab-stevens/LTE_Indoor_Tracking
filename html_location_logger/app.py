#! /bin/python3

import csv
from datetime import datetime, timedelta
from flask import Flask, render_template
from flask_socketio import SocketIO
import os

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Route to serve the HTML page
@app.route('/')
def home():
    columns = ['A', 'B', 'C', 'D']
    rows = list(range(8, 0, -1))
    return render_template("index.html", columns=columns, rows=rows)

# Log click to CSV
def log_click_to_csv(grid_index, click_time):
    date_str = datetime.now().strftime("%Y%m%d")
    folder_path = os.path.join("..", "logs", date_str)
    os.makedirs(folder_path, exist_ok=True)
    filename = os.path.join(folder_path, f"{date_str}_click_log.csv")
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Grid Index", "Click Time"])
        writer.writerow([grid_index, click_time])

# Calculate click counts
# def get_click_counts():
#     today = datetime.now().strftime("%Y%m%d")
#     #   = (datetime.now() - timedelta(days=2)).strftime("%Y%m%d")
#     counts = {"current": 0, "previous": 0}

#     for date, key in [(today, "current"), (yesterday, "previous")]:
#         folder_path = os.path.join("..", "logs", date)
#         print(folder_path)
#         filename = os.path.join(folder_path, f"{date}_click_log.csv")
#         print(filename)
#         if os.path.isfile(filename):
#             print('is filename')
#             with open(filename, 'r') as file:
#                 reader = csv.reader(file)
#                 counts[key] = sum(1 for _ in reader) - 1
#     print (counts)
#     return counts

# def get_click_counts():
#     logs_dir = os.path.join("..", "logs")
#     counts = {}
    
#     if not os.path.exists(logs_dir):
#         print("Logs directory not found.")
#         return counts

#     # Get all folder names in the logs directory
#     log_dates = sorted([d for d in os.listdir(logs_dir) if os.path.isdir(os.path.join(logs_dir, d))], reverse=True)
    
#     # Get the last 5 folder dates
#     last_5_dates = log_dates[:5]
    
#     for date in last_5_dates:
#         folder_path = os.path.join(logs_dir, date)
#         filename = os.path.join(folder_path, f"{date}_click_log.csv")
#         print(f"Checking file: {filename}")
#         if os.path.isfile(filename):
#             with open(filename, 'r') as file:
#                 reader = csv.reader(file)
#                 next(reader, None)  # Skip the header
#                 counts[date] = sum(1 for _ in reader)
#         else:
#             counts[date] = 0  # No file for this date

#     print(counts)
#     return counts

def get_click_counts():
    logs_dir = os.path.join("..", "logs")
    counts = {}
    
    if not os.path.exists(logs_dir):
        print("Logs directory not found.")
        return counts

    log_dates = sorted(
        [d for d in os.listdir(logs_dir) if os.path.isdir(os.path.join(logs_dir, d)) and d.isdigit()],
        reverse=True
    )
    
    last_5_dates = log_dates[:5]
    for date in last_5_dates:
        folder_path = os.path.join(logs_dir, date)
        filename = os.path.join(folder_path, f"{date}_click_log.csv")
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip the header
                counts[date] = sum(1 for _ in reader)
        else:
            counts[date] = 0  # No file for this date

    # print(counts)  # Debug
    return [{"date": date, "count": counts[date]} for date in counts]  # Convert to array

# Handle click events
@socketio.on('click_event')
def handle_click_event(data):
    grid_index = data['gridIndex']
    click_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
    log_click_to_csv(grid_index, click_time)
    counts = get_click_counts()
    socketio.emit('update_click_history', {'message': f"Grid: {grid_index} - Time: {click_time}"})
    print(counts)
    socketio.emit('update_click_counts', counts)

# Run the app
if __name__ == '__main__':
    socketio.run(app, host='192.168.1.13', port=5000, debug=True)