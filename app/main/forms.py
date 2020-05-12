from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Enter Your Name', validators=[Required()])
    room = StringField('Enter the Group ID', validators=[Required()])
    submit = SubmitField('Start Your GroupChat')
