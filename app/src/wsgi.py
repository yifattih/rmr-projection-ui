import os
from .routes import app

"""
Entry point to run the Flask application.

Environment Variables:
- PORT: The port number to run the application on (default: 5000).

"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
