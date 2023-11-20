from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Initialize click count
click_count = 0
json_file_path = "click_count.json"

# Load existing click count from JSON file
try:
    with open(json_file_path, "r") as file:
        click_count_data = json.load(file)
        click_count = click_count_data.get("click_count", 0)
except FileNotFoundError:
    # If the file is not found, create a new one
    with open(json_file_path, "w") as file:
        json.dump({"click_count": click_count}, file)

@app.route('/')
def index():
    return render_template('index.html', click_count=click_count)

@app.route('/click')
def click():
    global click_count
    click_count += 1

    # Update the JSON file with the new click count
    with open(json_file_path, "w") as file:
        json.dump({"click_count": click_count}, file)

    return jsonify({"click_count": click_count})

if __name__ == '__main__':
    app.run(debug=True)
