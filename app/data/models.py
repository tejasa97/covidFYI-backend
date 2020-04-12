from app import db
from datetime import date, datetime
from sqlalchemy import and_
from sqlalchemy.orm import load_only

class InfoType(db.Model):
    __tablename__ = 'info_type'

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(56), nullable=False)
    entries = db.relationship('Entry', backref='info_type', lazy='dynamic')

    description = db.Column(db.String(256), nullable=True)
    slug        = db.Column(db.String(32), nullable=True)
    active      = db.Column(db.Boolean, unique=False, default=True)

    def __str__(self):

        return f'{self.name}'

    @classmethod
    def get_or_save(self, name, description='', active=True):

        info_type = InfoType.query.filter_by(name=name).first()
        if info_type is not None:
            return info_type, False
        
        info_type = InfoType(name=name, description=description, active=active)
        info_type.save()

        return info_type, True

    def save(self):

        db.session.add(self)
        db.session.commit()

    def toJson(self):

        return {
            "name"        : self.name,
            "description" : self.description,
            "active"      : self.active
        }

class Location(db.Model):

    __tablename__ = 'location'

    id       = db.Column(db.Integer, primary_key=True)
    state    = db.Column(db.String(32), nullable=False)
    city     = db.Column(db.String(64), nullable=True)
    entries  = db.relationship('Entry', backref='location', lazy='dynamic')

    def __str__(self):
        return f'<{self.state}-{self.district}>'

    @classmethod
    def get_or_save(self, state, city):

        location = Location.query.filter_by(state=state, city=city).first()
        if location is not None:
            return location, False
        
        location = Location(state=state, city=city)
        location.save()

        return location, True

    def save(self):

        db.session.add(self)
        db.session.commit()

    def toJson(self):

        return {
            "name" : self.state,
            "city" : self.city,
        }

class Entry(db.Model):
    __tablename__ = 'entry'

    id          = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    infotype_id = db.Column(db.Integer, db.ForeignKey('info_type.id'), nullable=False)
    name        = db.Column(db.String(128), nullable=False, default='')
    occupation  = db.Column(db.String(128), nullable=True, default='')
    email_id_1  = db.Column(db.String(128), nullable=True, default = '')
    email_id_2  = db.Column(db.String(128), nullable=True, default = '')
    phone_1     = db.Column(db.String(128), nullable=True, default = '')
    phone_2     = db.Column(db.String(128), nullable=True, default = '')
    extension   = db.Column(db.String(128), nullable=True, default = '')
    source      = db.Column(db.String(128), nullable=False)
    source_link = db.Column(db.String(256), nullable=False)
    source_link_valid      = db.Column(db.Boolean, default=True)
    details     = db.Column(db.String(512), nullable=True, default = '')
    added_on    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self):
        return f'{self.name}'

    def save(self):

        db.session.add(self)
        db.session.commit()

    def toJson(self):

        return {
            "name"               : self.name,
            "occupation"         : self.occupation,          
            "email_id_1"         : self.email_id_1,
            "email_id_2"         : self.email_id_2,
            "phone_1"            : self.phone_1,
            "phone_2"            : self.phone_2,
            "extension"          : self.extension,
            "source"             : self.source, 
            "source_link"        : self.source_link,
            "source_link_valid"  : self.source_link_valid,
            "details"            : self.details,
        }