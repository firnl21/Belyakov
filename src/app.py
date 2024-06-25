from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from models import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




    
@app.route ('/perekus')
def perekus():
    return render_template('perekus.html')

@app.route ('/katalog')
def katalog():
    return render_template('katalog.html')

@app.route ('/base')
def base():
    return render_template('base.html')

@app.route ('/login')
def log():
    return render_template('login.html')

@app.route ('/register')
def reg():
    return render_template('register.html')

@app.route ('/nozhka')
def nozhka():
    return render_template('1nozhka.html')

@app.route ('/buiabes')
def buiabes():
    return render_template('2buiabes.html')

@app.route ('/aldente')
def aldente():
    return render_template('3aldente.html')

@app.route ('/luk')
def luk():
    return render_template('4luk.html')

@app.route ('/graten')
def graten():
    return render_template('5graten.html')

@app.route ('/zhulien')
def zhulien():
    return render_template('6zhulien.html')

@app.route ('/gov')
def gov():
    return render_template('7gov.html')

@app.route ('/shok')
def shok():
    return render_template('8shok.html')

@app.route ('/maff')
def maff():
    return render_template('9maff.html')

@app.route ('/kord')
def kord():
    return render_template('10kord.html')

@app.route ('/krev')
def krev():
    return render_template('11krev.html')

@app.route ('/kish')
def kish():
    return render_template('12kish.html')

@app.route ('/rat')
def rat():
    return render_template('13rat.html')

@app.route ('/gr')
def gr():
    return render_template('14gr.html')

@app.route ('/glint')
def glint():
    return render_template('15glint.html')







@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already taken')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', user=current_user)
    else:
        return redirect(url_for('register'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('register'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000, host="0.0.0.0")
