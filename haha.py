from flask import Flask, render_template, session, request, redirect, url_for
import pymysql

app = Flask(__name__)
app.secret_key = 'Any string'

db = pymysql.connect('localhost','Tiffany','Tiff_1019','GlobalSquashClub')



@app.route('/', methods = ['POST','GET'])
def index():
	#if 'email' in session:
		#return 'Logged in as ' + session['email'] + '<br>' + "<a href = '"
	return render_template("Index.html")

@app.route('/loginsubmit',methods = ['POST','GET'])
def login():
	#error = None


	if request.method == 'POST':
		email = request.form["email"]
		pwd = request.form['password']

		cursor = db.cursor()

		sql = ("SELECT password, userType, userName FROM users WHERE userEmail = '"+str(email)+"'")
		cursor.execute(sql)

		db.commit()

		results = cursor.fetchall()

		name = []
		userType = []
		password = []
		name_str = ''
		usertype_str = '' 

		for row in results:
			password.append(row[0])
			userType.append(row[1])
			name.append(row[2])

		

		if len(name) <1:
			errormessage = "**InvaildEmail"
			return render_template('Index.html', errorMessage = errormessage)
		else:

			name_str = name
			usertype_str = userType
			session['name'] = name[0]


			if pwd == password[0]:
				if userType[0] == '1':
					#return 'Hello %s' %name_str
					return redirect(url_for('employee'))
				else:
					#return 'no %s' %name_str
					return redirect(url_for('customer'))
			else:
				errormessage = "**wrongPassword"
				return render_template('Index.html', errormessage = errormessage)


	#return str(name) +str(userType) +str(password) + str(email)
	return redirect(url_for('index', name = name[0]))
	#return (str(results))





@app.route('/aboutUs')
def aboutUs():
	return render_template("AboutUs.html")

@app.route('/squash')
def squash():
	return render_template("Squash.html")

@app.route('/coaches')
def coaches():
	coach = {"coachId":[], "name":[], "phone":[], "email":[], "year_of_teaching":[], "coach_level":[]

	}
	cursor = db.cursor()

	sql = ("SELECT * FROM coaches ")
	cursor.execute(sql)

	db.commit()

	results = cursor.fetchall()
	for row in results:
		coach["coachId"].append(row[0])
		coach["name"].append(row[1])
		coach["phone"].append(row[2])
		coach["email"].append(row[3])
		coach["year_of_teaching"].append(row[4])
		coach["coach_level"].append(row[5])
		#session['name'] = name


	#return str(coach)
	return render_template("Coaches.html", coach = coach)

@app.route('/training')
def training():
	course = {"courseCode":[], "date":[], "avaliable_seats":[], "coaches":[]

	}
	cursor = db.cursor()

	sql = ("SELECT * FROM courses ")
	cursor.execute(sql)

	db.commit()

	results = cursor.fetchall()
	for row in results:
		course["courseCode"].append(row[0])
		course["date"].append(row[1])
		course["avaliable_seats"].append(row[2])
		course["coaches"].append(row[3])

	return render_template("Training.html", course = course)

@app.route('/contactUs')
def contactUs():
	return render_template("ContactUs.html")

@app.route('/comment', methods = ["POST"])
def comment():
	if request.method == 'POST':
		name = request.form["name"]
		email = request.form["email"]
		commentInfo = request.form["commentInfo"]

		cursor = db.cursor()

		sql = """INSERT INTO comment (commentName, commentEmail, commentInfo ) VALUES ('%s', '%s', '%s')"""%(str(name), str(email), str(commentInfo))

		cursor.execute(sql)
		db.commit()

	return render_template('ContactUs.html')

@app.route('/employee')
def employee():
	return render_template("Employee.html")

@app.route('/coachRegisterSubmit', methods = ["POST"])
def coachRegisterSubmit():
	if request.method == 'POST':
		name = request.form["name"]
		phone = int(request.form["phone"])
		email = request.form["email"]
		year_of_teaching = int(request.form["year_of_teaching"])
		coach_level = int(request.form["coach_level"])

		cursor = db.cursor()

		sql = """INSERT INTO coaches (name, phone, email, year_of_teaching, coach_level) VALUES ('%s', %d, '%s',%d, %d )"""%(str(name), int(phone), str(email), int(year_of_teaching), int(coach_level))

		cursor.execute(sql)
		db.commit()

	#return str(name)
	return render_template("Employee.html")

@app.route('/userRegisterSubmit', methods = ["POST"])
def userRegisterSubmit():
	if request.method == 'POST':
		name = request.form["name"]
		phone = int(request.form["phone"])
		email = request.form["email"]
		date_of_birth = request.form["date_of_birth"]
		
		userType = request.form["userType"]
		password = request.form['password']

		sql1 = """SELECT userName, userEmail FROM users """ 

		user ={"userName":[], "userEmail":[]}

		cursor = db.cursor()

		cursor.execute(sql1)
		db.commit()

		results = cursor.fetchall()
		error = False

		for row in results:
			user["userName"].append(row[0])
			user["userEmail"].append(row[1])

		for i in range(len(user["userName"])):

			if name == user["userName"][i]:
				error=True
				return ("error")
		for i in range(len(user["userEmail"])):

			if email == user["userEmail"][i]:
				error=True
				return ("error")

		if error == False:


			if userType == "employee":
				db_userType = 1
			else:
				db_userType = 2

			cursor = db.cursor()

			sql="""INSERT INTO users (userName, contactNo, userEmail, password, dateOfBirth, userType) VALUES ('%s',%d,'%s','%s','%s','%s')"""%(str(name), int(phone),str(email),str(password),str(date_of_birth),str(db_userType))

			#sql = """INSERT INTO users (userName, contactNo, userEmail, password, dateOfBirth, userType) VALUES ('%s',%d,'%s','%s','%s',%d)"""%(str(name),int(phone),str(email),str(password),str(date_of_birth),int(userType))
				#'" +name+ "', " +phone+" , '" +email+"' , '" +date_of_birth+ "', '"+str(db_userType)+"', '"+password+"')") 
			cursor.execute(sql)

			db.commit()
		
		

	#return str(userName)+ str(userEmail)	
	return render_template("Employee.html")

@app.route('/commentPage')
def commentPage():
	commentPage = {"commentCode":[], "commentName":[], "commentEmail":[], "commentInfo":[]

	}
	
	cursor = db.cursor()

	sql = ("SELECT * FROM comment ")
	cursor.execute(sql)


	db.commit()

	results = cursor.fetchall()

	for row in results:
		commentPage["commentCode"].append(row[0])
		commentPage["commentName"].append(row[1])
		commentPage["commentEmail"].append(row[2])
		commentPage["commentInfo"].append(row[3])

	return render_template("Employee.html", commentPage = commentPage[0])
	#return str(commentPage) 
	#return redirect(url_for('employee', commentPage = commentPage))



@app.route('/customer')
def customer():
	#return "Hello %s !" %name
	return render_template("Customer.html")

@app.route('/courseC001Register', methods = ['POST'])
def courseC001Register():
	if request.method == 'POST':
		name = request.form["userName"]
		

		cursor = db.cursor()
		error = False

		userName = []
		sql1 = """SELECT name FROM c001"""
		cursor.execute(sql1)
		db.commit()

		result = cursor.fetchall()
		for row in result:
			userName.append(row[0])

		for i in range(len(userName)):
			if name == userName[i]:
				error = True
				errorMessage = "Repeat registed"
				return render_template("Customer.html", errorMessage = errorMessage)
			else:
				error=False

				sql = """INSERT INTO c001 (name) VALUES ('%s') """%(str(name))

				cursor.execute(sql)
				db.commit()

		



	return render_template("Customer.html")
	#return (str(name))
@app.route('/courseC002Register', methods = ['POST'])
def courseC002Register():
	if request.method == 'POST':
		name = request.form["userNames"]
		

		cursor = db.cursor()
		

		userName = []
		sql1 = """SELECT name FROM c002"""
		cursor.execute(sql1)
		db.commit()

		result = cursor.fetchall()
		for row in result:
			userName.append(row[0])
		if len(userName) >0:

			for i in range(len(userName)):
				if name == userName[i]:
										
					errorMessage = "Repeat registed"
					return render_template("Customer.html", errorMessage = errorMessage)
				else:
	
					sql2 = """INSERT INTO c002 (name) VALUES ('%s') """%(str(name))
	
					cursor.execute(sql2)
					db.commit()
		else:
			sql = """INSERT INTO c002 (name) VALUES ('%s') """%(str(name))
	
			cursor.execute(sql)
			db.commit()


	return render_template("Customer.html")
	#return (str(userName))

@app.route('/logout')
def logout():
	session.pop("name",None)
	return render_template("Index.html")



if __name__ == '__main__':
	app.run(debug = True)