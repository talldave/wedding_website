from flask import render_template, url_for, redirect, request, flash, session
#from flask.ext.login import login_user, logout_user, current_user, login_required
from flask_mail import Message
from wedding_site.app import app, mail
from models import db, Guest, Rsvp, GuestRsvp, LoginTable, Venue, Event_V, Web_Content
from forms import LoginForm, RsvpForm, PasswordForm
#import logging

@app.route('/')
@app.route('/index.html')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/index-test')
def indextest():
    content = Web_Content.query.filter_by(page='home').all()
    return render_template('index-test.html', content=content)

@app.route('/testredir')
def rdir():
    return redirect(url_for('notfound'))

@app.route('/testemailthankyou')
def test_email_thank_you():
    rsvp_response0 = GuestRsvp.query.filter_by(id=session['guestid']).first()
    rsvp_response1 = GuestRsvp.query.filter_by(group=session['group']).all()
    return render_template('rsvp-thank-you-email.html', rsvp0=rsvp_response0, rsvpr=rsvp_response1)

@app.route('/error-on-purpose')
def erroronpurpose():
    db.session.comit()
    return "Hello, Error!"

@app.route('/test')
def test():
    return "Hello, World!"

@app.route('/testdb')
def testdb():
    #if db.session.query("1").from_statement("SELECT 1").all():
    guest = Guest.query.filter_by(id=1).first()
    rsvpr = Rsvp.query.filter_by(guest_id=999).first()
    guests = Guest.query.filter_by(group=session['group']).all()
    guest_count = Guest.query.filter_by(group=session['group']).count()
    t = Rsvp(888,1,'Hello','friday','morning',1,0)
    db.session.add(t)
    db.session.commit()

    if guest:
    #if rsvpr:
        #print "Guest ID:", guest.id
        #print "hello ", guest.salutation
        #return 'It works.'
        return render_template('testdb.html', guest=guest, rsvpr=rsvpr, guests=guests, guest_count=guest_count)
        #return render_template('testdb.html', guest=guest)
    else:
        return 'Something is broken.'

#@app.route('/login-test')
#@login_required
#def logtest():
    #return "This is the login test page"

@app.route('/invite', methods=['GET', 'POST'])
def invite():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('invitation'))
        else:
            return render_template('index.html')
    return render_template('login.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            t = LoginTable('',session['guestid'],request.remote_addr)
            db.session.add(t)
            db.session.commit()
            if 'adminlogin' in session:
                session.pop('adminlogin', None)
            #if session['guestid'] in ("1","2"):
                return redirect(url_for('password'))
            else:
                return redirect(url_for('rsvp'))
    return render_template('login.html', form=form)

@app.route('/schedule')
def sched():
    return render_template('schedule.html')

@app.route('/schedule-test')
def schedtest():
    events = Event_V.query.order_by(Event_V.start_date.asc()).all()
    return render_template('schedule-test.html', events=events)

@app.route('/password', methods=['GET', 'POST'])
def password():
    form = PasswordForm()
    if request.method == 'POST':
        if form.validate():
            session['admin'] = 1
            return redirect(url_for('rsvp'))
        else:
            #session.pop('admin', None)
            #return redirect(url_for('index'))
            return redirect(url_for('logout'))

    return render_template('password.html', form=form)

@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
    form = RsvpForm()
    if 'guestid' not in session:
        return redirect(url_for('login'))
    guests = Guest.query.filter_by(group=session['group']).all()

    if request.method == 'POST' and form.validate():
        #if form.validate_on_submit():
            #testg = Rsvp(2, 1, 'friday','afternoon',0)
            #return testg
            #db.session.add(testg)
            msg = Message("Thank you for your RSVP", sender=("Name", "email@example.com"))
            msg.bcc = ("groom@example.com","bride@example.com")
            for i in guests:
                msg.add_recipient(i.email_address)
                #return i.id
                #gid = i.id
                #logging.debug("this is i.id: ", i.id)
                #rsvpi = Rsvp(gid, form.i['id'].data, form.arrival_date.data, form.arrival_time.data, form.child_care.data, 1)
                radioname = "guest" + str(i.id)
                radval = form[radioname].data
                radval = str(radval)
 		if radval not in ('0','1'): radval = -1
                #if i.id == session['guestid']: session['response'] = radval
                ccval = form.child_care.data
                if ccval not in ('0','1'): ccval = -1
                rsvpi = Rsvp(i.id, radval, form.notebox.data, form.arrival_date.data, form.arrival_time.data, ccval, 1 )
                db.session.add(rsvpi)
            db.session.commit()
            rsvp_response0 = GuestRsvp.query.filter_by(id=session['guestid']).first()
            rsvp_response1 = GuestRsvp.query.filter_by(group=session['group']).all()
            #msg.body = "Insert receipt email here" # text body
            msg.body = render_template('rsvp-thank-you-email.txt', rsvp0=rsvp_response0, rsvpr=rsvp_response1)
            msg.html = render_template('rsvp-thank-you-email.html', rsvp0=rsvp_response0, rsvpr=rsvp_response1)
            mail.send(msg)
            return redirect(url_for('rsvp'))
        #else:
            #return "Didn't work"

    glist = []
    for j in guests:
        glist.append(j.id)

    rsvp_response0 = GuestRsvp.query.filter_by(id=session['guestid']).first()
    rsvp_response = GuestRsvp.query.filter_by(group=session['group']).all()
    for r in rsvp_response:
        if r.id == session['guestid']:
            session['response'] = r.response

    if rsvp_response:
        return render_template('rsvp-thank-you.html', rsvpr=rsvp_response, guests=guests, glist=glist, rsvp0=rsvp_response0)

    return render_template('rsvp.html', form=form, guests=guests)

@app.route('/change-rsvp')
def change_rsvp():
    guests = Guest.query.filter_by(group=session['group']).all()
    glist = []
    for j in guests:
        glist.append(j.id)
    rsvp_response = Rsvp.query.filter(Rsvp.guest_id.in_(glist)).filter(Rsvp.final==1).all()
    for r in rsvp_response:
        r.final = 0
    db.session.commit()
    return redirect(url_for('rsvp'))


@app.route('/logout')
def logout():
    session.pop('guestid', None)
    session.pop('salutation', None)
    session.pop('group', None)
    session.pop('user', None)
    session.pop('response', None)
    session.pop('admin', None)
    return redirect(url_for('index'))

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/travel/staying-here-test')
def stayhere_test():
    staymain = Web_Content.query.filter_by(page='staying-here').filter_by(section='main').all()
    staytypes = Web_Content.query.filter_by(page='staying-here').all()
    return render_template('staying-here-test.html', staytypes=staytypes, staymain=staymain)

@app.route('/travel/staying-here')
def stayhere():
    return render_template('staying-here.html')

@app.route('/travel/getting-here-test')
def gethere_test():
    transtypes = Web_Content.query.filter_by(page='getting-here').all()
    return render_template('getting-here-test.html', transtypes=transtypes)

@app.route('/travel/getting-here')
def gethere():
    return render_template('getting-here.html')

@app.route('/travel/getting-around')
def getaround():
    return render_template('getting-around.html')

@app.route('/registry')
def registry():
    return render_template('registry.html')

@app.route('/local-info/explore-sonoma')
def explore_sonoma():
    return render_template('explore-sonoma.html')

@app.route('/local-info/explore-sf')
def explore_sf():
    return render_template('explore-sf.html')

@app.route('/local-info/weather')
def weather():
    return render_template('weather.html')

@app.route('/local-info/maptest', methods=['GET', 'POST'])
def maptest():
    if request.method == 'POST':
        pass
    venues = Venue.query.all()
    return render_template('maptest.html', venues=venues)

@app.route('/local-info/maps')
def maps():
    return render_template('maps.html')

@app.route('/trk')
def trk():
    guest_id = request.args['gid']
    page_req = request.args['p']

    guest = Guest.query.filter_by(track_num = guest_id).first()
    #guest = 1

    if guest:
        session['guestid'] = guest.id
        session['salutation'] = guest.salutation
        session['group'] = guest.group
        return redirect(url_for('invitation'))
    else:
        return redirect(url_for('invite'))

#@login_required
@app.route('/invitation')
def invitation():
    if 'guestid' in session:
        return render_template('invitation.html')

    return redirect(url_for('index'))

@app.route('/admin')
#@authDB.requires_auth
def admin():
    #session['user'] = request.authorization.username
    return render_template('admin/index.html')

@app.route('/view-guest-list')
def view_guest_list():
    yes = GuestRsvp.query.filter_by(response=1).count()
    no = GuestRsvp.query.filter_by(response=0).count()
    noresp = 142 - (yes + no)
    guests = GuestRsvp.query.order_by(GuestRsvp.response.desc()).order_by(GuestRsvp.rsvp_date).all()
    #guests = Rsvp.query.filter_by(final=1).all()
    return render_template('admin/view-guest-list.html', guests=guests, yes=yes, no=no, noresp=noresp)

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/notfound')
def notfound():
    return render_template('notfound.html')

@app.route('/testrsvp')
def testrsvp():
    return render_template('rsvp_test.html')

@app.errorhandler(500)
def server_error(error):
    return render_template('error_500.html'), 500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404



