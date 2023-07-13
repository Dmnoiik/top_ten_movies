
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Length

class EditForm(FlaskForm):
    rating_field = DecimalField('Your rating out of 10?', places=1, validators=[DataRequired()])
    review_field = StringField('New review?', validators=[DataRequired()])
    submit_field = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField("Title of the movie", validators=[DataRequired()])
    year = IntegerField("Year of production", validators=[DataRequired()])
    description = StringField("Short description", validators=[DataRequired()])
    rating = DecimalField("Rating", validators=[DataRequired()])
    ranking = IntegerField("Ranking position", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    img_url = StringField("Link to cover image", validators=[DataRequired()])
    submit_field = SubmitField('Add movie')

