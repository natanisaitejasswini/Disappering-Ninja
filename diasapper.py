from flask import Flask, render_template 
app = Flask(__name__)   
@app.route('/')                                 
def no_ninja():
  return render_template('diaspper.html')
@app.route('/ninja')
def all_ninja():
	return render_template('allninjas.html' ,filename1='static/img/donatello.jpg',filename2='static/img/leonardo.jpg',
		filename3='static/img/michelangelo.jpg', filename4='static/img/raphael.jpg')
@app.route('/ninja/<type>')
def blue_ninja(type):
	if type == 'blue':
		image = 'img/donatello.jpg'
	elif type == 'orange':
		image = 'img/leonardo.jpg'
	elif type == 'red':
		image = 'img/michelangelo.jpg'
	elif type == 'purple':
		image = 'img/raphael.jpg'
	else:
		image = 'img/notapril.jpg'
	return render_template('blueninja.html', file= image)

app.run(debug=True)
