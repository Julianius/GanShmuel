from flask import Flask, render_template
from script import script
app = Flask(__name__)

@app.route("/monitor")
def monitor():
    script()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)