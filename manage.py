#coding=utf-8

from nowstagram import app,db
from flask_script import Manager
from nowstagram.models import User,Image,Comment
import random
import unittest
from sqlalchemy import or_,and_

manager=Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User'+str(i+1),'a'+str(i)))
        for j in range(0,3):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('This is a commnet'+str(k),1+3*i+j,i+1))

    db.session.commit()


    # for i in range(50,100,2):
    #     user=User.query.get(i)
    #     user.username='[New]'+user.username
    # User.query.filter_by(id=51).update({'username':'[New2]'})
    # db.session.commit()


    # for i in range(50,100,2):
    #     comment=Comment.query.get(i+1)
    #     db.session.delete(comment)
    # db.session.commit()

    # print 1,User.query.all()
    # print 2,User.query.get(3)
    # print 3,User.query.filter_by(id=5).first()
    # print 4,User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    # print 5,User.query.filter(User.username.endswith('0')).limit(3).all()
    # print 6,User.query.filter(or_(User.id==88,User.id==99)).all()
    # print 7,User.query.filter(and_(User.id>88,User.id<93)).all()
    # print 8,User.query.filter(and_(User.id>88,User.id<93)).first_or_404()
    # print 9,User.query.order_by(User.id.desc()).paginate(page=1,per_page=10).items
    # user=User.query.get(1)
    # print 10,user.images
    #
    # image=Image.query.get(1)
    # print 11,image,image.user
@manager.command
def run_test():
    db.drop_all()
    db.create_all()
    tests=unittest.TestLoader().discover('./')
    unittest.TextTestRunner().run(tests)
if __name__ == '__main__':
    manager.run()