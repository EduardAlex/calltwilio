from flask import Flask, request, redirect, url_for, render_template
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import os

app = Flask(__name__)

@app.route("/")
def index():
	return redirect("/call")

@app.route("/call")
def callpage():
	return render_template("call.html")

@app.route("/call", methods=['POST'])
def call():
	sid = os.environ.get("SID_T")
	token = os.environ.get("TOKEN_T")
	client = Client(sid, token)
	number = request.form['number']
	text = request.form['text']
	twimlcall = VoiceResponse()
	twimlcall.say(text, voice="Polly.Carmen", language="ro-RO")
	print(str(twimlcall))
	call = client.calls.create(from_ = "+12055832852", to = number, twiml = str(twimlcall))
	return redirect("/call")

if __name__ == '__main__':
	app.run(debug = 1, host="0.0.0.0", port=80)