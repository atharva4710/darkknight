import os
from flask import Flask, render_template

# Load environment variables from .env file (if it exists)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed; use system environment variables

# Basic Flask app for Plansphere.ai
app = Flask(__name__)

# Configs via environment (sensible defaults for local development)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///timetable.db')
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME', 'plansphere')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'change-me')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    # For local development; in production Vercel will handle launching
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
