from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Note

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template("base.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': True, 'redirect': url_for('dashboard')})
            return redirect(url_for('dashboard'))
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': False, 'message': 'Login failed. Please check your credentials.'})
            flash('Login failed. Please check your credentials.')

    return render_template("index.html", page='login')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': False, 'message': 'Email already exists.'})
            flash('Email already exists.')
            return redirect(url_for('register'))

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user, remember=True)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': True, 'redirect': url_for('dashboard')})
        return redirect(url_for('dashboard'))

    return render_template("index.html", page='register')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/dashboard")
@login_required
def dashboard():
    all_notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", name=current_user.name, notes=all_notes)

@app.route("/add-note", methods=['GET', 'POST'])
@login_required
def add_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        new_note = Note(title=title, content=content, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added successfully!')
        return redirect(url_for('dashboard'))

    return render_template("create_note.html")

@app.route("/update-note/<int:id>", methods=['GET', 'POST'])
@login_required
def update_note(id):
    note = Note.query.get_or_404(id)
    if note.user_id != current_user.id:
        flash("You can't update this note!")
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        db.session.commit()
        flash('Note updated successfully!')
        return redirect(url_for('dashboard'))

    return render_template("create_note.html", note=note)

@app.route("/delete-note/<int:id>")
@login_required
def delete_note(id):
    note = Note.query.get_or_404(id)
    if note.user_id != current_user.id:
        flash("You can't delete this note!")
        return redirect(url_for('dashboard'))
    
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted!')
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)