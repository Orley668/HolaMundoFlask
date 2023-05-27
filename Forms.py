from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
#Create a new form class This form will be used for editing the content


class AboutForm(FlaskForm):
 content = TextAreaField('Content', validators=[DataRequired()])
 submit = SubmitField('Save')