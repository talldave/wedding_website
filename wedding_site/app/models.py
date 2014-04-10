from flask.ext.sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(filename='~/flask_env/sqldebug.log')
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

db = SQLAlchemy()

class Guest(db.Model):
    __tablename__ = 'GUEST'

    id = db.Column(db.Integer, primary_key = True)
    track_num = db.Column(db.String(7))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email_address = db.Column(db.String(64))
    salutation = db.Column(db.String(64))
    group = db.Column(db.String(64))

    def __init__(self, id, track_num, first_name, last_name, email_address, salutation, group):
        self.id = id
        self.track_num = track_num
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email_address = email_address.lower()
        self.salutation = salutation.title()
        self.group = group.lower()


class Rsvp(db.Model):
    __tablename__ = 'RSVP'

    id = db.Column(db.Integer, primary_key = True)
    guest_id = db.Column(db.Integer)
    response = db.Column(db.Integer)
    note = db.Column(db.String(4000))
    arrival_date = db.Column(db.String(24))
    arrival_time = db.Column(db.String(24))
    child_care = db.Column(db.Integer)
    final = db.Column(db.Integer)

    def __init__(self, guest_id, response, note, arrival_date, arrival_time, child_care, final ):
        self.guest_id = guest_id
        self.response = response
	self.note = note
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.child_care = child_care
        self.final = final

class GuestRsvp(db.Model):
    __tablename__ = 'GUEST_RSVP_V'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    response = db.Column(db.Integer)
    group = db.Column(db.String(64))
    child_care = db.Column(db.Integer)
    arrival_date = db.Column(db.String(24))
    arrival_time = db.Column(db.String(24))
    final = db.Column(db.Integer)
    note = db.Column(db.String())
    rsvp_date = db.Column(db.String(24))


    def __init__(self, first_name, last_name, group, response, arrival_date, arrival_time, child_care, final ):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.group = group.lower()
        self.response = response
        self.child_care = child_care
        self.arrival_date = arrival_date.lower()
        self.arrival_time = arrival_time.lower()
        self.final = final

class Venue(db.Model):
    __tablename__ = 'VENUE'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    address_id = db.Column(db.Integer)
    type = db.Column(db.String())
    phone = db.Column(db.String())

    def __init__(self, name, address_id, type, phone):
        self.name = name
        self.address_id = address_id
        self.type = type
        self.phone = phone

class LoginTable(db.Model):
    __tablename__ = 'LOGIN'

    id = db.Column(db.Integer, primary_key = True)
    email_not_found = db.Column(db.String(64))
    guest_id = db.Column(db.Integer)
    ip_addr = db.Column(db.String(16))

    def __init__(self, email_not_found, guest_id, ip_addr):
        self.email_not_found = email_not_found
        self.guest_id = guest_id
        self.ip_addr = ip_addr


class Event_V(db.Model):
    __tablename__ = 'EVENT_V'

    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.String(24))
    end_date = db.Column(db.String(24))
    #venue_id = db.Column(db.Integer)
    name = db.Column(db.String(128))
    description = db.Column(db.String(4096))
    venue_name = db.Column(db.String(64))
    venue_phone = db.Column(db.String(16))
    addr_street1 = db.Column(db.String(64))
    addr_street2 = db.Column(db.String(64))
    addr_city = db.Column(db.String(64))
    addr_state = db.Column(db.String(2))
    addr_zip = db.Column(db.String(10))
    streetview_link = db.Column(db.String(256))

    def __init__(self, start_date, end_date, venue_id, name, description):
        self.start_date = start_date
        self.end_date = end_date
        self.venue_id = venue_id
        self.name = name
        self.description = description

class Web_Content(db.Model):
    __tablename__ = 'WEB_CONTENT'

    id = db.Column(db.Integer, primary_key = True)
    page = db.Column(db.String(32))
    section = db.Column(db.String(32))
    content = db.Column(db.String(4096))
    fkey = db.Column(db.Integer)

