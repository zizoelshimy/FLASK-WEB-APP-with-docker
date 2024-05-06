from flask import Blueprint,render_template,redirect,url_for
views = Blueprint('views' , __name__)

@views.route('/')
def redirec():
   return redirect(url_for('views.login'))

@views.route('/login')
def login():
   return render_template('login.html')