from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, HiddenField, SelectField, StringField, SubmitField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  InputRequired, Length, ValidationError

class CreateTodoForm(FlaskForm):
    description = StringField(validators=[InputRequired(), Length(min=5)])
    submit = SubmitField('Create')

class TodoForm(FlaskForm):
    method = HiddenField()
    id = HiddenField()
    complete = BooleanField()
    description = StringField(validators=[InputRequired()])
    list_id = SelectField(coerce=int, choices=[], validate_choice=False)
    submit = SubmitField('Update')

#Registrierungs-Form hinzugefügt
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=5, max=30)], render_kw={"placeholder": "username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=5, max=25)], render_kw={"placeholder": "password"})

    submit = SubmitField("REGISTER")
        
#Login-Form hinzugefügt        
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=5, max=30)], render_kw={"placeholder": "username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=5, max=25)], render_kw={"placeholder": "password"})

    submit = SubmitField("LOGIN")

#Account löschen-Form hinzugefügt
class DeleteAccount(FlaskForm):
    submit = SubmitField('DELETE ACCOUNT')