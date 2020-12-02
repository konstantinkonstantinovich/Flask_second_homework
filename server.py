from flask import Flask, render_template, url_for
from faker import Faker
import csv
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/getfile') # task 1 requirements.txt
def getfile():
	t = url_for('static', filename='requirements.txt')
	l = list() # empty list filled with data from file
	with open('.' + t) as r:
		for i in r:
			l.append(i)
	return render_template('first_task.html', l = l) 


@app.route('/name_plus_emails') # task 2 names and emails
@app.route('/name_plus_emails/<int:len_names>')
def get_name_and_emails(len_names=100):
	fake = Faker()
	if type(len_names) == int:
		if len_names <= 100:
			names = [fake.unique.first_name() for i in range(len_names)] # list of random names
			emails = [fake.ascii_company_email() for i in range(len_names)] # list of random emails
			a = dict(zip(names, emails)) # a dictionary in which the key is a list of names, and the values ​​are a list of emails
		else:
			return 'The len of name out of range!'
	else:
		return 'The value of the entered number is not int!'

	return render_template('second_task.html', a = a)


@app.route('/parse_file') # task 3 the average amont 
def parse_file():
	g = url_for('static', filename='hw.csv')
	with open('.' + g) as t:
		reader = csv.reader(t, delimiter = ',', skipinitialspace=True)
		sum_sm = 0
		sum_kg = 0
		num = 0
		for r in reader:
			if len(r)!=0 and r[0].isdigit(): 
				sum_sm += float(r[1])
				sum_kg += float(r[2])
			num+=1
		avg_sm = (sum_sm * 2.54)/num
		avg_kg = (sum_kg * 0.454)/num
		lis = list() # an empty list to fill it with the results of the function execution
		lis.append(avg_sm)
		lis.append(avg_kg)
	return render_template('third_task.html', lis = lis)


@app.route('/space') # task 4 the number of astronauts
def space():
	r = requests.get('http://api.open-notify.org/astros.json') # link from where to get data
	r.json()["number"]
	return render_template('forths_task.html', r = r)




