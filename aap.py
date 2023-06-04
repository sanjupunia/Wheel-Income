from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <body>
    <h1>Hello World!!</h1>
    <p>Test site.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
