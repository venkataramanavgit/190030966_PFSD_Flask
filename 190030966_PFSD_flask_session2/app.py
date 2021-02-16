from flask import Flask,render_template
app= Flask(__name__)
@app.route('/')
def home():
	return render_template('/home.html',tittle="new home")

@app.route('/appointment')
def appointment():
	return render_template('/appointment.html')

@app.route('/contactus')
def contactus():
	return render_template('/contactus.html')
