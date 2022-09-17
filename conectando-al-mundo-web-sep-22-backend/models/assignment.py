from marshmallow_sqlalchemy import SQLAlchemySchema
from models.shared import db
from models.user_has_assignment import UserHasAssignment
class Assignment(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    due_date=db.Column(db.DateTime,nullable=False)
    users = db.relationship('User', secondary = 'user_has_assignment')

    def save(self):
        db.session.add(self)
        db.session.commit()

class AssignmentSchema(SQLAlchemySchema):
    class Meta:
        fields = ('id', 'name', 'due_date')
        model = Assignment
        load_instance = True
