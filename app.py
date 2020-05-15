from flask import Flask, request, redirect, url_for, render_template
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/")
def index():
	return redirect("/call")

@app.route("/call")
def callpage():
	return render_template("call.html")

@app.route("/call", methods=['POST'])
def call():
	client = Client('AC4ba293b6b9d6b3f2ef3ec18141a4c60e','19ec34fff4d59f0d5dea008c14be7b92')
	number = request.form['number']
	text = request.form['text']
	twimlcall = VoiceResponse()
	twimlcall.say(text)
	print(str(twimlcall))
	call = client.calls.create(from_ = "+12055832852", to = number, twiml = str(twimlcall))
	return redirect("/call")

if __name__ == '__main__':
	app.run(debug = 1, host="0.0.0.0", port=80)