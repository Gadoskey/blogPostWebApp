from flask_wtf import FlaskForm as Form
from flask_wtf.file import FileField, FileAllowed
from flaskblog.models import User
from flask_login import current_user
from wtforms import StringField as MyString, PasswordField as MyPassword, SubmitField as MySubmit, BooleanField as MyBoolean, TextAreaField
from wtforms.validators import DataRequired as Required, Length, Email, EqualTo, ValidationError

""" 
Sign up class
The EqualTo in the confirm password field ensures that the 
input in that section matches with the password field 
"""
class RegistrationForm(Form):
    username = MyString('Username', validators=[Required(), Length(min=2, max=22)])
    email = MyString('Email', validators=[Required(), Email()])
    password = MyPassword('Password', validators=[Required()])
    confirm_password = MyPassword('Confirm Password', validators=[Required(), EqualTo('password')])
    submit = MySubmit('Sign Up')
  
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Exists! Please Input a New Username')
  
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email Exists! Please Input a New Email')
  
""" 
Login class
"""
class LogInForm(Form):
    email = MyString('Email', validators=[Required(), Email()])
    password = MyPassword('Password', validators=[Required()])
    remember_password = MyBoolean('Remember Password')
    submit = MySubmit('Sign In')

# Note: Secret keys protect against forgery attacks.
# You can do this by adding app.config['SECRET_KEY'] = value in your app.
# You can set your custom key or get some from Python using secrets.token_hex(number_of_digits_wanted).
# Remember to import secrets before doing that.

class UpdateForm(Form):
    username = MyString('Username', validators=[Required(), Length(min=2, max=22)])
    email = MyString('Email', validators=[Required(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = MySubmit('Update Account')
  
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username Exists! Please Input a New Username')
  
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email Exists! Please Input a New Email')
            
class RequestPasswordReset(Form):
    email = MyString('Email', validators=[Required(), Email()])
    submit = MySubmit('Request Password Reset')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Email Does Not Exist! Sign Up Now')

class PasswordReset(Form):
    password = MyPassword('Password', validators=[Required()])
    confirm_password = MyPassword('Confirm Password', validators=[Required(), EqualTo('password')])
    submit = MySubmit('Reset Password')


class BioForm(Form):
    bio = TextAreaField('Your Bio', validators=[Required()])
    submit = MySubmit('Update Bio')