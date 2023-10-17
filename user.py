#from app import db
#from flask_login import UserMixin

#class User(db.Model, UserMixin):
  #  id = db.Column(db.Integer, primary_key=True)
   # username = db.Column(db.String(50), unique=True, nullable=False)
   # password = db.Column(db.String(100), nullable=False)

#class RegisterForm(FlaskForm):
   # username = StringField(validators=[InputRequired(), Length(
    #    min=5, max=30)], render_kw={"placeholder": "Benutzername"})

   # password = PasswordField(validators=[InputRequired(), Length(
   #     min=5, max=25)], render_kw={"placeholder": "Passwort"})

  #  submit = SubmitField("Registrieren") #muss ich hier register nhemen wegen des Klassennamens oder ist das egal?


  #  def validate_username(self, username):
  #      existing_user_username = User.query.filter_by(
   #         username=username.data).first()
        
    #    if existing_user_username:
    #        raise ValidationError(
    #            "Dieser Benutzername existiert bereits. Bitte nehmen Sie einen anderen Namen!"
    #        )

#class LoginForm(FlaskForm):
 #   username = StringField(validators=[InputRequired(), Length(
 #       min=5, max=30)], render_kw={"placeholder": "Benutzername"})

  #  password = PasswordField(validators=[InputRequired(), Length(
  #      min=5, max=25)], render_kw={"placeholder": "Passwort"})

  #  submit = SubmitField("Login")



    #@staticmethod
   # def add_user(username, password):
      #  new_user = User(username=username, password=password)
      #  db.session.add(new_user)
      #  db.session.commit()

 #   @staticmethod
   # def get(user_id):
   #     return User.query.get(user_id)