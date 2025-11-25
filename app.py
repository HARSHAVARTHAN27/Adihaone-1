"""
Root-level Flask app entry point for Vercel deployment.
Imports the actual app from the nested backend location.
"""
import sys
import os

# Add the backend directory to the path so we can import the app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ai_assistant', 'backend'))

# Import the Flask app from the backend
from app import app

# Export the app for Vercel
__all__ = ['app']
