from . import db

class Logs(db.Model):
    __tablename__ = "logs"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    log = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "log": self.log,
            "author": self.author
        }