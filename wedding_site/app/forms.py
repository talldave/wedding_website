from flask import session, request
from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, RadioField, HiddenField, SelectField, TextAreaField, PasswordField, validators
from wtforms.validators import InputRequired, Email, Optional
from models import db, Guest, Rsvp, LoginTable

class PasswordForm(Form):
    password = PasswordField("Please enter your password", validators = [InputRequired()])
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        if self.password.data == 'notverysecret':
            return True
        else:
            self.password.errors.append("* Invalid password. *")
            return False

class ScheduleForm(Form):
    date = SelectField()
    time = SelectField('', validators=[Optional()], choices=[('','Select a time'),('friday','Friday'),('saturday','Saturday'),('sunday','Sunday')])
    name = TextField("Enter the event name:", validators = [InputRequired()])
    desc = TextAreaField("Enter the event description:", validators = [InputRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

class LoginForm(Form):
    email = TextField("Please enter your email address to continue:", validators = [InputRequired(), Email()])
    submit = SubmitField("Enter")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        guest = Guest.query.filter_by(email_address = self.email.data.lower()).first()

        if guest:
            session['guestid'] = guest.id
            session['salutation'] = guest.salutation
            session['group'] = guest.group
            if guest.id in (1,2):  session['adminlogin'] = 1
            return True
        else:
            self.email.errors.append("* Your email address was not found.  Please try again or contact us. *")
            t = LoginTable(self.email.data,999,request.remote_addr)
            db.session.add(t)
            db.session.commit()
            return False

class RsvpForm(Form):
    #guest1 = RadioField('', [validators.InputRequired(message=u'* Please choose a response for all guests *')], choices=[('1','YES'), ('0','NO')])
    guest1 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest2 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest3 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest600 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest601 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest602 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest603 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest604 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest605 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest606 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest607 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest608 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest609 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest610 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest611 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest612 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest613 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest614 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest615 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest616 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest617 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest618 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest619 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest620 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest621 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest622 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest623 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest624 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest625 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest626 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest627 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest628 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest629 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest630 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest631 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest632 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest633 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest634 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest635 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest636 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest637 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest638 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest639 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest640 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest641 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest642 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest643 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest644 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest645 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest646 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest647 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest648 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest649 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest650 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest651 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest652 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest653 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest654 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest655 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest656 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest657 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest658 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest659 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest660 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest661 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest662 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest663 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest664 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest665 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest666 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest667 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest668 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest669 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest670 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest671 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest672 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest673 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest674 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest675 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest676 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest677 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest678 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest679 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest680 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest681 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest682 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest683 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest684 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest685 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest686 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest687 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest688 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest689 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest690 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest691 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest692 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest693 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest694 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest695 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest696 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest697 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest698 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest699 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest700 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest701 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest702 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest703 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest704 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest705 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest706 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest707 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest708 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest709 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest710 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest711 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest712 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest713 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest714 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest715 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest716 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest717 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest718 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest719 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest720 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest721 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest722 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest723 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest724 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest725 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest726 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest727 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest728 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest729 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest730 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest731 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest732 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest733 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest734 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest735 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest736 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest737 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest738 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest739 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest740 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest741 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest742 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest743 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest744 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest745 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest746 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest747 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest748 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest749 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest750 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest751 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest752 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest753 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest754 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest755 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest756 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest757 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest758 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])
    guest759 = RadioField('', [validators.Optional()], choices=[('1','YES'), ('0','NO')])



    notebox = TextAreaField()
    arrival_date = SelectField('',validators=[Optional()],choices=[('n/a','Please select a date'),('Not sure','I don\'t know yet'),('Before Friday','Before Friday'), ('Friday','On Friday'), ('Saturday','On Saturday'), ('Sunday','On Sunday')])
    arrival_time = SelectField('',validators=[Optional()],choices=[('','Please select a time'),('morning','Morning'),('afternoon','Afternoon'),('evening','Evening')])
    child_care = RadioField('Are you interested in Child Care?', validators=[Optional()],choices=[('1','Yes'), ('0','No')])
    submit = SubmitField("Submit RSVP")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True

