from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "Hydrate Yourself right now!!"

app.run(host="0.0.0.0",port=80) ##or 5001    