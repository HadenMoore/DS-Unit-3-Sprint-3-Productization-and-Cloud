# Import my flash package
from flask import Flask, render_template

# Create Flask Web Server
app = Flask(__name__)

# Route Determines Location
@app.route("/")

# Define a littel function to-
# Tell it what to do at that Route
def home():
    return render_template('home.html')

# Create another route
@app.route("/about")

#Define another Function for this New route
def pred():
    return render_template('about.html')

# Clean things up
if __name__ == "__main__":
    app.run(debug=True)

#to run this go to terminal and type python myapp.py
#alt approach to running it, also in terminal:
# FLASK_APP= myapp.py flask run
