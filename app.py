from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "AKS Working with DevOps Pipeline!"

app.run(host="0.0.0.0", port=5000)
