from project_name import db


class NameModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
