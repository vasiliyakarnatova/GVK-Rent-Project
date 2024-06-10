from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import Client, Staff
from . import db

auth = Blueprint('auth', __name__)

@auth.route("/Signin", methods=['POST', 'GET'])
def login():
    form_id = request.form.get("form_id")
    
    if request.method == "POST" and form_id == "signin":
        email = request.form.get("email_l")
        password = request.form.get("password_l")
        role = request.form.get('role')

        if role == 'Staff':
            existing_user = Staff.query.filter_by(staff_email=email).first()
            
            if existing_user and existing_user.staff_password == password:
                session['email'] = email
                session['role'] = role
                return redirect(url_for('views.index'))
            else:
                flash("Invalid account", category="error")
        elif role == 'Client':
            existing_user = Client.query.filter_by(client_email=email).first()
            if existing_user and existing_user.client_password == password:
                session['email'] = email
                session['role'] = role

                return redirect(url_for('views.index'))
            else:
                flash("Invalid account", category="error")
        else:
            flash("Requred role", category="error")

    elif request.method == "POST" and form_id == "signup":
        email = request.form.get("email_r")
        password = request.form.get("password_r")
        username = request.form.get("username")
        number = request.form.get("number")

        if Client.query.filter_by(client_email=email).first():
            return redirect('/Signin')

        highest_id = db.session.query(db.func.max(Client.id)).scalar()
        next_id = (highest_id or 0) + 1

        new_client = Client(id=next_id, client_name=username, client_phone_number=number, client_address='Sofia', client_email=email, client_password=password)
        db.session.add(new_client)
        db.session.commit()
        
        session['email'] = email
        session['role'] = 'Client'

        return redirect(url_for('views.index'))
        
    return render_template("login.html")

@auth.route('/Logout')
def logout():
    redirect_if_not_users()

    session.clear()
    return redirect(url_for('views.index'))

@auth.route('/users')
def show_users():
    from .models import Staff, Client

    redirect_if_not_users()

    clients = Client.query.all()
    staff = Staff.query.all()

    return render_template('users.html', clients=clients, staff=staff)

def redirect_if_not_users():
    if not session.get('email'):
        return redirect('/Signin')