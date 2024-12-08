import os
from .routes import app

"""
Entry point to run the Flask application.

Environment Variables:
- PORT: The port number to run the application on (default: 4000).

"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(debug=False, host="0.0.0.0", port=port)
