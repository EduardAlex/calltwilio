from flask import Flask, request, redirect, url_for, render_template
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import os

app = Flask(__name__)

langs = {}
with open("langs.txt", "r") as f:
	for line in f.readlines():
		p = line.split("/")
		langs[p[0]] = [p[1],p[2],p[3]]

@app.route("/")
def index():
	return redirect("/call")

@app.route("/call")
def callpage():
	return render_template("call.html", langs = langs)

@app.route("/call", methods=['POST'])
def call():
	sid = os.environ.get("SID_T")
	token = os.environ.get("TOKEN_T")
	client = Client(sid, token)
	number = request.form['number']
	text = request.form['text']
	twimlcall = VoiceResponse()
	language = request.form['language']
	twimlcall.say(text, voice=langs[language][2], language=langs[language][3])
	print(str(twimlcall))
	call = client.calls.create(from_ = "+12055832852", to = number, twiml = str(twimlcall))
	return redirect("/call")

if __name__ == '__main__':
	app.run(debug = 1, host="0.0.0.0", port=80)