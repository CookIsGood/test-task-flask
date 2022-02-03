from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
import re


def check_animal_name(form, field):
    match = re.fullmatch(r"[a-zA-Z]{5,20}", field.data)
    if not match:
        raise ValidationError('Animal name contains invalid characters!')


class SearchForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired(message="You have not filled in the name field!")],
                       render_kw={
                           'id': 'name',
                       })

    submit = SubmitField("Search!")


class CreateAnimal(FlaskForm):
    name_animal = StringField('Name: ', validators=[DataRequired(message="You did not fill in the name field!"),
                                                    Length(min=2, max=30,
                                                           message="The length of the animal name must be "
                                                                   "between 2 and 30 characters!"), check_animal_name])
    type_animal = SelectField('Type: ',
                              choices=[('Млеко', 'Млекопитающие'), ('НеМлеко', 'НеМлекопитающие')])
    speed_animal = IntegerField('Speed: ', validators=[DataRequired(message="You have not filled out the speed field!"),
                                                       NumberRange(min=1, max=1000,
                                                                   message="The speed of the animal can be from 1 to 1000!")])
    predator_animal = SelectField('Predator: ',
                                  choices=[(True, 'Хищник'), (False, 'НеХищник')])

    submit = SubmitField("Create!")
