from flask import Flask
from flask_sqlalchemy import SQLAlchemy, session
from flask_session import Session
from os import path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

db = SQLAlchemy()
DB_NAME = 'database_final.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BD Project'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Office, Staff, Client, Property, Apartment, House, OtherProperty

    with app.app_context():
        db.create_all()
        defaull_offices()
        #print_all_offices()
        default_staff()
        #print_staff()

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

def defaull_offices():
    from .models import Office

    offices = [
        {'office_name': 'Младост 1', 'office_address': 'Младост 1 ул. "Иван Шишман" 10'},
        {'office_name': 'Лозенец', 'office_address': 'ул. "Крум Попов" 14'},
        {'office_name': 'Малинова долина', 'office_address': 'ул. "Симеоновско шосе" 21'},
        {'office_name': 'Дружба 1', 'office_address': 'ул. "Обиколна" 8'},
        {'office_name': 'Овча купел', 'office_address': 'ул. "Монтевидео" 34'},
        {'office_name': 'Студентски град', 'office_address': 'ул. "Акад. Стефан Младенов" 4'},
        {'office_name': 'Бояна', 'office_address': 'ул. "Панорамен път" 31'},
        {'office_name': 'Люлин 6', 'office_address': 'ул. "Златна Добруджа" 5'},
    ]
    
    for office in offices:
        existing_office = Office.query.filter_by(office_name=office['office_name']).first()
        if not existing_office:
            new_office = Office(office_name=office['office_name'], office_address=office['office_address'])
            db.session.add(new_office)
    
    db.session.commit()

def print_all_offices():
    from .models import Office

    offices = Office.query.all()
    for office in offices:
        print(f"Office Name: {office.office_name}, Office Address: {office.office_address}")

def print_staff():
    from .models import Staff

    staff = Staff.query.all()
    for emp in staff:
        print(f"Emp Name: {emp.staff_name}, Emp Num: {emp.staff_phone_number}")

def default_staff():
    from .models import Staff

    staff_members = [
        {'id': 1113, 'staff_name': 'Петар Иванов', 'staff_phone_number': '0889090787', 'staff_email': 'petar@abv.bg', 'working_office': 'Овча купел', 'staff_password': 'petar1'},
        {'id': 1114, 'staff_name': 'Георги Георгиев', 'staff_phone_number': '0898922782', 'staff_email': 'georgi@abv.bg', 'working_office': 'Лозенец', 'staff_password': 'georgi1'},
        {'id': 1115, 'staff_name': 'Чандлър Бинг', 'staff_phone_number': '0876636791', 'staff_email': 'mati@abv.bg', 'working_office': 'Студентски град', 'staff_password': 'mati1'},
        {'id': 1116, 'staff_name': 'Цвети Боянова', 'staff_phone_number': '0887878937', 'staff_email': 'stefi@abv.bg', 'working_office': 'Малинова долина', 'staff_password': 'cveti1'},
        {'id': 1117, 'staff_name': 'Красимира Банкова', 'staff_phone_number': '0895558337', 'staff_email': 'krasi@abv.bg', 'working_office': 'Бояна', 'staff_password': 'krasi1'},
        {'id': 1118, 'staff_name': 'Християн Димитров', 'staff_phone_number': '0895558352', 'staff_email': 'hridim@abv.bg', 'working_office': 'Дружба 1', 'staff_password': 'hridim1'},
        {'id': 1119, 'staff_name': 'Богдан Богданов', 'staff_phone_number': '0895558352', 'staff_email': 'gogi@abv.bg', 'working_office': 'Люлин 6', 'staff_password': 'gogi1'},
        {'id': 1120, 'staff_name': 'Владимир Стоянов', 'staff_phone_number': '0895668352', 'staff_email': 'vladi@abv.bg', 'working_office': 'Люлин 6', 'staff_password': 'vladi1'}
    ]

    for staff in staff_members:
        existing_staff = Staff.query.filter_by(id=staff['id']).first()
        if not existing_staff:
            new_staff = Staff(
                id=staff['id'],
                staff_name=staff['staff_name'],
                staff_phone_number=staff['staff_phone_number'],
                staff_email=staff['staff_email'],
                working_office=staff['working_office'],
                staff_password=staff['staff_password']
            )
            db.session.add(new_staff)

    db.session.commit()

    
# def default_staff_users():
#     from .models import UserStaff

#     staff_members = [
#         {'staff_id': 1113, 'user_name': 'petar@abv.bg', },
#         {'staff_id': 1114, 'user_name': 'georgi@abv.bg', },
#         {'staff_id': 1115, 'user_name': 'mati@abv.bg',},
#         {'staff_id': 1116, 'user_name': 'stefi@abv.bg'},
#         {'staff_id': 1117, 'user_name': 'krasi@abv.bg'},
#         {'staff_id': 1118, 'user_name': 'hridim@abv.bg'},
#         {'staff_id': 1119, 'user_name': 'gogi@abv.bg'},
#         {'staff_id': 1120, 'user_name': 'vladi@abv.bg'}
#     ]

#     for staff in staff_members:
#         existing_staff = UserStaff.query.filter_by(staff_id=staff['staff_id']).first()
#         if not existing_staff:
#             new_staff = UserStaff(
#                 staff_id=staff['staff_id'],
#                 user_name=staff['user_name'],
#                 user_password=staff['user_password']
#             )
#             db.session.add(new_staff)

#     db.session.commit()