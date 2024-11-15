from routes import app

"""
This is the main file that starts the flask server and serves the web app UI
in the browser.

"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
