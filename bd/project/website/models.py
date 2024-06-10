from . import db

class Office(db.Model):
    __tablename__ = 'offices'
    
    office_name = db.Column(db.String(100), primary_key=True, nullable=False)
    office_address = db.Column(db.String(200), nullable=False)
    
    staff = db.relationship('Staff', back_populates='office')

class Staff(db.Model):
    __tablename__ = 'staff'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    staff_name = db.Column(db.String(100), nullable=False)
    staff_phone_number = db.Column(db.CHAR(10), nullable=False)
    staff_email = db.Column(db.String(30))
    staff_password = db.Column(db.String(20), nullable=False)

    working_office = db.Column(db.String(200), db.ForeignKey('offices.office_name'))
    office = db.relationship('Office', back_populates='staff')

class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    client_phone_number = db.Column(db.CHAR(10), nullable=False)
    client_address = db.Column(db.String(200), nullable=False)
    client_email = db.Column(db.String(30))
    client_password = db.Column(db.String(20), nullable=False)

    properties = db.relationship('Property', back_populates='owner')

class Property(db.Model):
    __tablename__ = 'properties'
    
    address = db.Column(db.String(200), primary_key=True, nullable=False)
    type = db.Column(db.String(30), nullable=False)
    location = db.Column(db.String(200))
    rent = db.Column(db.Float, nullable=False)
    area = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000))
    
    owner_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    owner = db.relationship('Client', back_populates='properties')
    
    apartments = db.relationship('Apartment', back_populates='property')
    houses = db.relationship('House', back_populates='property')
    other_properties = db.relationship('OtherProperty', back_populates='property')

class Apartment(db.Model):
    __tablename__ = 'apartments'
    
    apartment_type = db.Column(db.String(30), nullable=False)
    construction = db.Column(db.String(30))
    flat = db.Column(db.Integer, nullable=False)
    construction_year = db.Column(db.Integer, nullable=False)
    garage = db.Column(db.CHAR(1))
    parking_slot = db.Column(db.CHAR(1))
    finished = db.Column(db.CHAR(1))
    repairs = db.Column(db.CHAR(1))
    pet_friendly = db.Column(db.CHAR(1))
    
    apartments_address = db.Column(db.String(200), db.ForeignKey('properties.address'), primary_key=True)
    property = db.relationship('Property', back_populates='apartments')

class House(db.Model):
    __tablename__ = 'houses'
    
    house_type = db.Column(db.String(30), nullable=False)
    construction = db.Column(db.String(30))
    construction_year = db.Column(db.Integer)
    garage = db.Column(db.CHAR(1))
    parking_slot = db.Column(db.CHAR(1))
    yard = db.Column(db.CHAR(1))
    land = db.Column(db.CHAR(1))
    finished = db.Column(db.CHAR(1))
    repairs = db.Column(db.CHAR(1))
    pet_friendly = db.Column(db.CHAR(1))
    
    houses_address = db.Column(db.String(200), db.ForeignKey('properties.address'), primary_key=True)
    property = db.relationship('Property', back_populates='houses')

class OtherProperty(db.Model):
    __tablename__ = 'other_properties'
    
    other_properties_type = db.Column(db.String(30), nullable=False)
    flat = db.Column(db.Integer, nullable=False)
    
    other_properties_address = db.Column(db.String(200), db.ForeignKey('properties.address'), primary_key=True)
    property = db.relationship('Property', back_populates='other_properties')

# db version 01
# class Office(db.Model):
#     __tablename__ = 'offices'

#     office_name = db.Column(db.String(100), primary_key=True, nullable=False)
#     office_address = db.Column(db.String(200), nullable=False)

#     # Relationship to Staff
#     staff = db.relationship('Staff', back_populates='working_office')

# class Staff(db.Model):
#     __tablename__ = 'staff'

#     staff_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     staff_name = db.Column(db.String(100), nullable=False)
#     staff_phone_number = db.Column(db.String(10), nullable=False)
#     staff_email = db.Column(db.String(30))
#     working_office = db.Column(db.String(200), db.ForeignKey('offices.office_name'))

#     # Relationship to Office
#     office = db.relationship('Office', back_populates='staff')

#     # Relationship to Owner
#     owner = db.relationship('Owner', back_populates='staff', uselist=False)

#     # Relationship to Contract
#     contracts = db.relationship('Contract', back_populates='staff')

# # class Client(db.Model):
# #     __tablename__ = 'clients'

# #     clients_id = db.Column(db.Integer, primary_key=True, nullable=False)
# #     clients_name = db.Column(db.String(100), nullable=False)
# #     clients_phone_number = db.Column(db.String(10), nullable=False)
# #     clients_address = db.Column(db.String(200), nullable=False)

# #     # Relationship to Property
# #     properties = db.relationship('Property', back_populates='owner')

# #     # Relationship to Contract
# #     contracts = db.relationship('Contract', back_populates='client')

# # class Owner(db.Model):
# #     __tablename__ = 'owners'

# #     employee_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), primary_key=True)

# #     # Relationship to Staff
# #     staff = db.relationship('Staff', back_populates='owner')

# class Property(db.Model):
#     __tablename__ = 'properties'

#     address = db.Column(db.String(200), primary_key=True, nullable=False)
#     type = db.Column(db.String(30), nullable=False)
#     location = db.Column(db.String(200))
#     rent = db.Column(db.Float, nullable=False)
#     area = db.Column(db.Integer, nullable=False)
#     description = db.Column(db.String(1000))
#     owner_id = db.Column(db.Integer, db.ForeignKey('clients.clients_id'))

#     # Relationship to Client
#     owner = db.relationship('Client', back_populates='properties')

#     # Relationships to Property Types
#     apartments = db.relationship('Apartment', back_populates='property', uselist=False)
#     houses = db.relationship('House', back_populates='property', uselist=False)
#     other_properties = db.relationship('OtherProperty', back_populates='property', uselist=False)

# # class Contract(db.Model):
# #     __tablename__ = 'contract'

# #     id = db.Column(db.Integer, primary_key=True)
# #     contract_date = db.Column(db.Date)
# #     contract_rent = db.Column(db.Float)
# #     contract_expiration_date = db.Column(db.Date)
# #     conditions = db.Column(db.String(300))
# #     client_id = db.Column(db.Integer, db.ForeignKey('clients.clients_id'))
# #     staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))

# #     # Relationship to Client
# #     client = db.relationship('Client', back_populates='contracts')

# #     # Relationship to Staff
# #     staff = db.relationship('Staff', back_populates='contracts')

# class Apartment(db.Model):
#     __tablename__ = 'apartments'

#     apartment_type = db.Column(db.String(30), nullable=False)
#     construction = db.Column(db.String(30))
#     flat = db.Column(db.Integer, nullable=False)
#     construction_year = db.Column(db.Integer, nullable=False)
#     garage = db.Column(db.String(1))
#     parking_slot = db.Column(db.String(1))
#     finished = db.Column(db.String(1))
#     repairs = db.Column(db.String(1))
#     pet_friendly = db.Column(db.String(1))
#     apartments_address = db.Column(db.String(200), db.ForeignKey('properties.address'), primary_key=True)

#     # Relationship to Property
#     property = db.relationship('Property', back_populates='apartments')

# class House(db.Model):
#     __tablename__ = 'houses'

#     house_type = db.Column(db.String(30), nullable=False)
#     construction = db.Column(db.String(30))
#     construction_year = db.Column(db.Integer)
#     garage = db.Column(db.String(1))
#     parking_slot = db.Column(db.String(1))
#     yard = db.Column(db.String(1))
#     land = db.Column(db.String(1))
#     finished = db.Column(db.String(1))
#     repairs = db.Column(db.String(1))
#     pet_friendly = db.Column(db.String(1))
#     houses_address = db.Column(db.String(200), db.ForeignKey('properties.address'), primary_key=True)

#     # Relationship to Property
#     property = db.relationship('Property', back_populates='houses')

# class OtherProperty(db.Model):
#     __tablename__ = 'other_properties'

#     other_properties_type = db.Column(db.String(30), nullable=False)
#     flat = db.Column(db.Integer, nullable=False)
#     other_properties_address = db.Column(db.String(200), db.ForeignKey('properties.address'), primary_key=True)

#     # Relationship to Property
#     property = db.relationship('Property', back_populates='other_properties')

# class UserClient(db.Model, UserMixin):
#     __tablename__ = 'user_client'

#     user_email = db.Column(db.String(50), primary_key=True, nullable=False)
#     user_password = db.Column(db.String(20), nullable=False)
#     client_id = db.Column(db.Integer, db.ForeignKey('clients.clients_id'))

#     # Relationship to Client
#     client = db.relationship('Client')

# class UserStaff(db.Model, UserMixin):
#     __tablename__ = 'user_staff'

#     user_email = db.Column(db.String(50), primary_key=True, nullable=False)
#     user_password = db.Column(db.String(20), nullable=False)
#     staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))

#     # Relationship to Staff
#     staff = db.relationship('Staff')