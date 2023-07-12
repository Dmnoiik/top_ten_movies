from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EditForm(FlaskForm):
    rating_field = StringField('Your rating out of 10?', validators=[DataRequired()])
    review_field = StringField('New review?', validators=[DataRequired()])
    submit_field = SubmitField('Done')
