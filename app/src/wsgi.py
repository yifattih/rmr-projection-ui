import os
from routes import app

"""
This is the main file that starts the flask server and serves the web app UI
in the browser.

"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
