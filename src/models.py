from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integeer,primary_key=True)
    favorite_character_id = db.Column(db.Integer,db.ForeignKey("character.id")) #find out more about primary key and foreign key
    favorite_planet_id = db.Column(db.Integer, db.ForeignKey("Planet.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    user = db.relationship("User",foreign_keys = [user_id])
    favorite_character = db.relationship("Character", foreignkeys = [favorite_character_id])
    favorite_planet = db.relationship("Planet", foreignkeys = [favorite_planet_id])


    class Character(db.Model):
        __tablename__ = "Character"
        id - db.Column(db.Integer, primary_key =True)
        name = db.Column(db.String(200))
        description = db.Column(db.String(400))
def serialize(self):
    return {
        "id":self.id,
        "name":self.name,
        "description": self.description
    }
                                   