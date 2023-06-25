from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_pic = db.Column(db.String, unique=False, nullable=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False) 

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "profile_pic": self.profile_pic,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f'<Role {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
# Tabla auxiliar para enlazar rol(role) y usuario(user)
class User_role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship(Role)

    # def serialize(self):
    #     user_info = User.query.filter_by(id=self.user_id).first()

    def __repr__(self):
        return f'<Role {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "role": self.role_id,
            "user": self.user_id,
            # "user_info": user_info.serialize()
        }
    
class Pro_profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    description = db.Column(db.String(255), unique=False, nullable=False)
    address = db.Column(db.String(200), unique=False, nullable=True)
    postal_code = db.Column(db.Numeric, unique=False, nullable=False)
    phone_number = db.Column(db.Numeric, unique=False, nullable=True)
    hourly_rate = db.Column(db.Numeric, unique=False, nullable=False)

    def __repr__(self):
        return f'<Pro_profile {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "address": self.address,
            "postal_code": self.postal_code,
            "phone_number": self.phone_number,
            "hourly_rate": self.hourly_rate
        }

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=False, nullable=False)

    def __repr__(self):
        return f'<Skill {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
# Tabla auxiliar para enlazar perfil(pro_profile) y habilidades(skills)
class Pro_profile_skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    skill = db.relationship(Skill)
    pro_profile_id = db.Column(db.Integer, db.ForeignKey('pro_profile.id'))
    pro_profile = db.relationship(Pro_profile)

    def __repr__(self):
        return f'<Pro_profile_skill {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "skills": self.skill_id,
            "pro_profile": self.pro_profile_id
        }
    
class Cmr_profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    description = db.Column(db.String(255), unique=False, nullable=False)
    phone_number = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f'<Cmr_profile {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "phone_number": self.phone_number
        }
    
class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_visible = db.Column(db.Boolean(), unique=False, nullable=False, default=False)
    name = db.Column(db.String(200), unique=False, nullable=True)
    address = db.Column(db.String(200), unique=False, nullable=True)
    postal_code = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    cmr_profile_id = db.Column(db.Integer, db.ForeignKey('cmr_profile.id'))
    cmr_profile = db.relationship(Cmr_profile)
    

    def __repr__(self):
        return f'<Home {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "address": self.address,
            "postal_code": self.postal_code,
            "description": self.description,
            "cmr_profile_id": self.cmr_profile_id
        }

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(60), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    size_sqm = db.Column(db.Integer)
    home_id = db.Column(db.Integer, db.ForeignKey('home.id'))
    home = db.relationship(Home)

    def __repr__(self):
        return f'<Room {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "description": self.description,
            "size_sqm": self.size_sqm,
            "home_id": self.home_id
        }
    
class Habitant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(60), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return f'<Habitant {self.id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "description": self.description
        }
    
# Tablas auxiliares para interconectar casas(homes) con sus habitaciones(rooms) 
# y habitantes(habitants), y las casas(homes) con los perfiles de clientes

class Cmr_profile_home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, db.ForeignKey('home.id'))
    home = db.relationship(Home)
    cmr_profile_id = db.Column(db.Integer, db.ForeignKey('cmr_profile.id'))
    cmr_profile = db.relationship(Cmr_profile)

    def __repr__(self):
        return f'<Cmr_profile_home {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "home": self.home_id,
            "cmr_profile": self.cmr_profile_id
        }
    
class Home_habitant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, db.ForeignKey('home.id'))
    home = db.relationship(Home)
    habitant_id = db.Column(db.Integer, db.ForeignKey('habitant.id'))
    habitant = db.relationship(Habitant)

    def __repr__(self):
        return f'<Home_habitant {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "home": self.home_id,
            "habitant": self.habitant_id
        }

class TimestampMixin(db.Model):
    __abstract__ = True
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

class JobStatus(Enum):
    PENDING = 'Pending'
    ACTIVE = 'Active'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'

class PaymentStatus(Enum):
    PENDING = 'Pending'
    PAYED = 'Payed'
    REFUNDED = 'Refunded'


class Contract(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, db.ForeignKey('home.id'))
    home = db.relationship(Home)
    pro_profile_id = db.Column(db.Integer, db.ForeignKey('pro_profile.id'))
    pro_profile = db.relationship(Pro_profile)
    cmr_profile_id = db.Column(db.Integer, db.ForeignKey('cmr_profile.id'))
    cmr_profile = db.relationship(Cmr_profile)
    job_status = db.Column(db.Enum(JobStatus), default=JobStatus.PENDING)
    payment_status = db.Column(db.Enum(PaymentStatus), default=PaymentStatus.PENDING)
    comment = db.Column(db.String(255), unique=False, nullable=True)
    job_date = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f'<Contract {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "home_id": self.home_id,
            "pro_profile_id": self.pro_profile_id,
            "cmr_profile_id": self.cmr_profile_id,
            "comment": self.comment,
            "job_date": self.job_date,
            "job_status": self.job_status,
            "payment_status": self.payment_current_status
        }

class Pro_review(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    pro_receiver_id = db.Column(db.Integer, db.ForeignKey('pro_profile.id'))
    pro_profile = db.relationship(Pro_profile)
    cmr_sender_id = db.Column(db.Integer, db.ForeignKey('cmr_profile.id'))
    cmr_profile = db.relationship(Cmr_profile)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'))
    contract = db.relationship(Contract)
    comment = db.Column(db.String(255), unique=False, nullable=False)


    def __repr__(self):
        return f'<Pro_review {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "pro_receiver_id": self.pro_receiver_id,
            "cmr_sender_id": self.cmr_sender_id,
            "contract_id": self.contract_id,
            "comment": self.comment
        }

class Cmr_review(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    pro_sender_id = db.Column(db.Integer, db.ForeignKey('pro_profile.id'))
    pro_profile = db.relationship(Pro_profile)
    cmr_receiver_id = db.Column(db.Integer, db.ForeignKey('cmr_profile.id'))
    cmr_profile = db.relationship(Cmr_profile)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'))
    contract = db.relationship(Contract)
    comment = db.Column(db.String(255), unique=False, nullable=False)


    def __repr__(self):
        return f'<Cmr_review {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "pro_sender_id": self.pro_sender_id,
            "cmr_receiver_id": self.cmr_receiver_id,
            "contract_id": self.contract_id,
            "comment": self.comment
        }

class MessageStatus(Enum):
    DRAFT = 'Draft'
    SENT = 'SENT'
    
class Message(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=False, nullable=False)
    content = db.Column(db.String(255), unique=False, nullable=False)
    message_status = db.Column(db.Enum(MessageStatus), default=MessageStatus.DRAFT)
    home_id = db.Column(db.Integer, db.ForeignKey('home.id'))
    home = db.relationship(Home)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)


    def __repr__(self):
        return f'<Message {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "home_id": self.home_id,
            "title": self.rating,
            "content": self.content,
            "message_status": self.message_status,
            "sender_id": self.sender_id
        }


class Message_receiver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    message = db.relationship(Message)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)


    def __repr__(self):
        return f'<Message_receiver {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "message_id": self.message_id,
            "receiver_id": self.receiver_id,
        }

