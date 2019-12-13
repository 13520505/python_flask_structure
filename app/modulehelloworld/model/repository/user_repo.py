# Import module models (i.e. User)
from app.modulehelloworld.model.entity.user  import User
from app import db


def get_user_by_name(name):
    user = User.query.filter_by(name=name).first()
    return user


def create_test_user():
    minh = User('minhha', 'minhha@gmail.com', '0123456789')
    la = User('anhnl', 'anhnl@gmail.com', '0987654321')
    db.session.add(minh)
    db.session.add(la)
    db.session.commit()
