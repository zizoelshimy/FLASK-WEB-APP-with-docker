from flask import Blueprint ,render_template,request,redirect,url_for,flash,session

from .models import Database
auth = Blueprint('auth' , __name__)

db = Database()
db.connect()
result = db.fetch_data()

checkedLoggedIn = False

def validate_login(email, password):
   return email == "example@example.com" and password == "password123"



@auth.route('/home',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            if validate_login(email, password):
                session['logged_in'] = True  
                return render_template('home.html')
            else:
                flash('Wrong Email or Password!', category='error')
                return redirect(url_for('views.login'))
        except:
            return redirect(url_for('views.login'))
    else:
        if 'logged_in' in session:
            return render_template('home.html')
        else:
            #flash('You need to login first!', category='error')
            #return redirect(url_for('views.login'))
            return render_template('error404.html')

@auth.route("/team")
def team():
    if 'logged_in' not in session or not session['logged_in']:
        #flash('You need to login first!', category='error')
        #return redirect(url_for('views.login'))
        return render_template('error404.html')
    return render_template("TeamP.html", data=result)
      
@auth.route("/logout",methods=['POST','GET'])
def logout():
    session.clear() 
    flash('You have been logged out.', category='success')
    return redirect(url_for('views.login'))
