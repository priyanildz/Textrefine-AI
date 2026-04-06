from flask import Blueprint, render_template, request, redirect, url_for, session
import csv
import os

auth = Blueprint('auth', __name__)

DATA_FILE = "data/user_data.csv"


# ✅ Ensure file exists
def create_file_if_not_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "email", "password"])


# ✅ REGISTER
@auth.route('/register', methods=['GET', 'POST'])
def register():
    create_file_if_not_exists()

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # check if user already exists
        with open(DATA_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username:
                    return render_template('register.html', error="Username already exists")

        # save user
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, email, password])

        return redirect(url_for('auth.login'))

    return render_template('register.html')


# ✅ LOGIN
@auth.route('/login', methods=['GET', 'POST'])
def login():
    create_file_if_not_exists()

    if request.method == 'POST':
        username = request.form['username'].strip().lower()
        password = request.form['password'].strip()

        with open(DATA_FILE, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['username'].strip().lower() == username and row['password'].strip() == password:
                    session['user'] = username
                    return redirect(url_for('auth.profile'))

        return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


# ✅ PROFILE
@auth.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    return render_template('profile.html', username=session['user'])


# ✅ LOGOUT
@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main.home'))