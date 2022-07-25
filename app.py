from flask import Flask

app = Flask(__name__)
print("test")


@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"
