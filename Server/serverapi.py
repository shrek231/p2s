from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/text')
def home():
	with open("Text.txt", "r") as f:
		sometext = f.readlines()
		return (sometext[0])

def run():
	app.run(
		host='0.0.0.0',
		port='8080'
		)

t = Thread(target=run)
t.start()
