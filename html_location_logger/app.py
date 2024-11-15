#! /bin/python3

from flask import Flask, render_template, request
from flask_socketio import SocketIO
from datetime import datetime
import csv
import os

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Route to serve the HTML page
@app.route('/')
def home():
    # Prepare the grid columns and rows
    columns = ['A', 'B', 'C', 'D']  # Column names A to D
    rows = list(range(8, 0, -1))    # Row numbers 8 to 1
    return render_template("index.html", columns=columns, rows=rows)

def log_click_to_csv(grid_index, click_time):
    # Create a filename based on the current date
    date_str = datetime.now().strftime("%Y%m%d")
    # Create a folder path ../log/yyyymmdd
    folder_path = os.path.join("..", "logs", date_str)
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Define the CSV file path inside the folder
    filename = os.path.join(folder_path, f"{date_str}_click_log.csv")
    
    # Check if the file exists
    file_exists = os.path.isfile(filename)

    # Open the file in append mode and write the data
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write the header only if the file is being created for the first time
        if not file_exists:
            writer.writerow(["Grid Index", "Click Time"])
        writer.writerow([grid_index, click_time])

# Handle click events
@socketio.on('click_event')
def handle_click_event(data):
    grid_index = data['gridIndex']
    click_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]
    click_message = f"Grid: {grid_index} - Time: {click_time}"
    
    # Log the click on the server
    print(click_message)
    log_click_to_csv(grid_index, click_time)
    # Send the click message to all connected clients
    socketio.emit('update_click_history', {'message': click_message})

# Run the app
if __name__ == '__main__':
    socketio.run(app, host='192.168.1.13', port=5000, debug=True)
    # app.run(host='192.168.1.13', port=5000, debug=True, threaded=False)