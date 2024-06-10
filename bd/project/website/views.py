from flask import Blueprint, render_template, session, request, flash
from .models import Property
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('ad_page.html', email=session.get('email'), role=session.get('role'), properties=Property.query.all())

@views.route('/Add_Property', methods=['POST', 'GET'])
def add_property():
    from .models import Property, House, Apartment, OtherProperty, Client
    
    if request.method == "POST":
        form_id = request.form.get('property_type')
        property_owner = request.form.get('property_owner')
        property_location = request.form.get('property_location')
        property_address = request.form.get('property_address')
        property_rent = request.form.get('property_rent')
        property_size = request.form.get('property_size')
        property_desc = request.form.get('property_description')

        new_property = Property(address=property_address, type=form_id, location=property_location, rent=property_rent, area=property_size, description=property_desc, owner_id=Client.query.filter_by(client_email=property_owner).first().id)

        if form_id == 'house':
            house_repair = request.form.get('house_repair')
            house_type = request.form.get('house_type')
            house_year = request.form.get('house_year')
            house_constr = request.form.get('house_construction')
            house_garage = request.form.get('garage')
            house_yard = request.form.get('yard')
            house_additional_land = request.form.get('additional_land')
            house_pets_allowed = request.form.get('pets_allowed')

            new_house = House(house_type=house_type, construction=house_constr, construction_year=house_year, garage=house_garage, parking_slot='F', yard=house_yard, land=house_additional_land, finished='T', repairs=house_repair, pet_friendly=house_pets_allowed, houses_address=property_address)

            print(new_house)
            print(new_property)

            db.session.add(new_property)
            db.session.add(new_house)
            db.session.commit()

        elif form_id == 'apartment':
            apartment_repair = request.form.get('apartment_repair')
            apartment_floor = request.form.get('apartment_floor')
            apartment_type = request.form.get('apartment_type')
            apartment_condition = request.form.get('apartment_condition')
            apartment_year = request.form.get('apartment_year')
            apartment_constr = request.form.get('apartment_construction')
            apartment_garage = request.form.get('garage')
            apartment_pets_allowed = request.form.get('pets_allowed')

            new_apartment = Apartment(apartment_type=apartment_type, flat=apartment_floor, construction=apartment_constr, construction_year=apartment_year, garage=apartment_garage, parking_slot='T', finished=apartment_condition, repairs=apartment_repair, pet_friendly=apartment_pets_allowed, apartments_address=property_address)
            print(new_apartment)
            print(new_property)
            db.session.add(new_property)
            db.session.add(new_apartment)
            db.session.commit()

        elif form_id == 'others':
            other_floor = request.form.get('other_floor')
            other_type = request.form.get('other_type')

            new_other = OtherProperty(flat=other_floor, other_properties_type=other_type, other_properties_address=property_address)
            print(new_other)
            print(new_other)
            db.session.add(new_property)
            db.session.add(new_other)
            db.session.commit()
        else:
            flash("Choose option", category="error")

    return render_template('AddProperty.html', email=session.get('email'), role=session.get('role'))

@views.route('/Properties')
def show_property():
    from .models import Client
    
    owner = Client.query.filter_by(client_email=session.get('email')).first()
    props = []
    
    if owner:
        props = Property.query.filter_by(owner_id=owner.id)

    return render_template('my_properties.html', email=session.get('email'), role=session.get('role'), properties=props)

@views.route('/Offices')
def show_offices():
    from .models import Office

    offices = Office.query.all()
    return render_template('Offices.html', offices=offices, email=session.get('email'), role=session.get('role'))

@views.route('/Staff')
def show_staff():
    from .models import Staff

    staff = Staff.query.all()
    return render_template('Staff.html', staff=staff, email=session.get('email'), role=session.get('role'))