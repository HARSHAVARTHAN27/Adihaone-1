"""
Root-level Flask app entry point for Vercel deployment.
Imports the actual app from the nested backend location.
"""
import sys
import os

# Add the backend directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ai_assistant', 'backend'))

# Change to backend directory so relative imports work
os.chdir(os.path.join(os.path.dirname(__file__), 'ai_assistant', 'backend'))

# Import the Flask application
from app import app as flask_app

# Export the app for Vercel
app = flask_app

if __name__ == '__main__':
    app.run()

