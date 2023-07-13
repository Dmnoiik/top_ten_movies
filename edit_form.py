import decimal

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Length

class EditForm(FlaskForm):
    rating_field = DecimalField('Your rating out of 10?', places=1, validators=[DataRequired()])
    review_field = StringField('New review?', validators=[DataRequired()])
    submit_field = SubmitField('Done')
