from flask import Flask
import asyncio
app = Flask(__name__)
loop = asyncio.get_event_loop()

@app.route('/')
def home():
    return "Hello Flask"
