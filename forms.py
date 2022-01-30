from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired(message="You have not filled in the name field!")],
                       render_kw={
                           'id': 'name',
                       })

    submit = SubmitField("Search!")
