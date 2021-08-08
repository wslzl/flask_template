from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)

    def get_schema(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
        }
