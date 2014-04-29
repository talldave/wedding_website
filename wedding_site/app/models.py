from flask.ext.sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(filename='~/flask_env/sqldebug.log')
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

db = SQLAlchemy()

class Guest(db.Model):
    __tablename__ = 'GUEST'

    id = db.Column(db.Integer, primary_key = True)
    track_num = db.Column(db.String(7), nullable=False, unique=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    email_address = db.Column(db.String(64))
    salutation = db.Column(db.String(64), nullable=False)
    group = db.Column(db.String(64), nullable=False)

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
    guest_id = db.Column(db.Integer, db.ForeignKey(Guest.id), nullable=False)
    response = db.Column(db.Integer, nullable=False, server_default=u"'-1'")
    note = db.Column(db.String(4000))
    arrival_date = db.Column(db.String(24), nullable=False)
    arrival_time = db.Column(db.String(24), nullable=False)
    child_care = db.Column(db.Integer, nullable=False, server_default=u"'-1'")
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
    name = db.Column(db.String(), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey(Address.id), nullable=False)
    type = db.Column(db.String(), nullable=False)
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
    guest_id = db.Column(db.Integer, db.ForeignKey(Guest.id))
    ip_addr = db.Column(db.String(16))

    def __init__(self, email_not_found, guest_id, ip_addr):
        self.email_not_found = email_not_found
        self.guest_id = guest_id
        self.ip_addr = ip_addr


class Event_V(db.Model):
    __tablename__ = 'EVENT_V'

    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
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
    page = db.Column(db.String(32), nullable=False)
    section = db.Column(db.String(32), nullable=False)
    content = db.Column(db.String(4096), nullable=False)
    fkey = db.Column(db.Integer)


class Address(db.Model):
    __tablename__ = 'ADDRESS'

    id = db.Column(db.Integer, primary_key = True)
    street1 = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip = db.Column(db.String(10), nullable=False)
    latitude = db.Column(db.Numeric(12,8))
    longitude = db.Column(db.Numeric(12,8))
    street2 = db.Column(db.String(64))
    streetview_link = db.Column(db.String(256))


class Vendor(db.Model):
    __tablename__ = 'VENDOR'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(16))
    web = db.Column(db.String(128))
    type = db.Column(db.String(32), nullable=False)


class Gift(db.Model):
    __tablename__ = 'GIFT'

    id = db.Column(db.Integer, primary_key = True)
    gift = db.Column(db.String(64), nullable=False)
    given_to = db.Column(db.String(128), nullable=False)
    given_from = db.Column(db.String(128), nullable=False)
    date_recd = db.Column(db.DateTime, nullable=False)
    ty_date_sent = db.Column(db.DateTime)


class Billing(db.Model):
    __tablename__ = 'BILLING'

    id = db.Column(db.Integer, primary_key = True)
    amt_est = db.Column(db.Numeric(8,2))
    amt_total = db.Column(db.Numeric(8,2), nullable=False)
    amt_owe = db.Column(db.Numeric(8,2), nullable=False)
    payee = db.Column(db.String(64), nullable=False)
    payor = db.Column(db.String(64), nullable=False)
    item = db.Column(db.String(128), nullable=False)


