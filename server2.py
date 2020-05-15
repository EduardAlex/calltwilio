from flask import Flask, request, redirect, url_for, render_template
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route('/generated/<text>')
def generatedcall(text):
	resp = VoiceResponse()
	resp.say(message=text,voice='alice')
	return str(resp)

@app.route('/')
def index():
	return render_template('call.html')

@app.route('/', methods=['GET'])
def getxml():
	phrase = request.args.get('text')
	return redirect(url_for('generatedcall', text=phrase))

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=8080)
