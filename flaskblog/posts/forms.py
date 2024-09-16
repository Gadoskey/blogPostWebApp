from flask_wtf import FlaskForm as Form
from wtforms import StringField as MyString, PasswordField as MyPassword, SubmitField as MySubmit, TextAreaField
from wtforms.validators import DataRequired as Required

  
class PostForm(Form):
    title = MyString('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = MySubmit('Post')