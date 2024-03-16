from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

# MongoDB connection setup
CONNECTION_STRING = f"mongodb+srv://{os.environ['USERNAME']}:{os.environ['PASSWORD']}@pocketdoccluster.dygbqiw.mongodb.net/pocketdocdb?retryWrites=true&w=majority&appName=pocketdoccluster"
client = MongoClient(CONNECTION_STRING)
db = client.your_database_name

@app.route('/')
def home():
    return "Hello, Flask with MongoDB!"

if __name__ == '__main__':
    app.run(debug=True)