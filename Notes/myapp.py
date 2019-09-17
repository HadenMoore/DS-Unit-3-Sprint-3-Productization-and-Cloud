# Import my flash package
from flask import Flask

# Create Flask Web Server
app = Flask(__name__)

# Route Determines Location
@app.route("/")

# Define a littel function to-
# -Tell it what to do at that Route
def home():
    return "What it do, Baby Boo?"

# Create another route
@app.route("/about")

#Define another Function for this New route
def pred():
    return "This is The About Page."

# Clean things up
if __name__ == "__main__":
    app.run(debug=True)

#to run this go to terminal and type python myapp.py
#alt approach to running it, also in terminal:
# FLASK_APP= myapp.py flask run
