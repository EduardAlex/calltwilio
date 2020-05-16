from flask import Flask, request, redirect, url_for, render_template
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import os

app = Flask(__name__)

languages = ["romanian/Romanian/Polly.Carmen/ro-RO",
	"english-us/English (US)/Polly.Salli/en-US",
	"english-uk/English (UK)/Polli.Amy/en-GB",
	"russian/Russian/Polli.Tatyana/ru-RU"]
langs = {}
#with open("langs.txt", "r") as f:
for line in languages:
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
	language = request.form['language']
	twimlcall = VoiceResponse()
	twimlcall.say(text, voice=langs[language][1], language=langs[language][2])
	print(str(twimlcall))
	call = client.calls.create(from_ = "+12055832852", to = number, twiml = str(twimlcall))
	return redirect("/call")

if __name__ == '__main__':
	app.run(debug = 1, host="0.0.0.0", port=80)