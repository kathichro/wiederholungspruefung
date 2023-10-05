from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    @staticmethod
    def add_user(username, password):
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def get(user_id):
        return User.query.get(user_id)

    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
