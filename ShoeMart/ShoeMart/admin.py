from flask import Blueprint
from . import db
from .models import Category, Shoe, Order
from datetime import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    c1 = Category(name='Men', image='men.jpg')
    c2 = Category(name='Women', image='women.jpg')
    c3 = Category(name='Kids', image='kidss.jpg')
    c4 = Category(name='sports_men')
    c5 = Category(name='casual_men')
    c6 = Category(name='heels_women')
    c7 = Category(name='sports_women')

    try:
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.add(c5)
        db.session.add(c6)
        db.session.add(c7)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    s1 = Shoe(category_id=c1.id, image='c1.jpg', price=22.00,
              date=datetime.now(),
               name='New Balance S-20',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')
    
    
    s2 = Shoe(category_id=c1.id, image='c2.jpg', price=23.00,
              date=datetime.now(),
               name='Lacoste-Pegasus',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s3 = Shoe(category_id=c1.id, image='c3.jpg', price=25.00,
              date=datetime.now(),
               name='Hush Puppies-HP30',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s4 = Shoe(category_id=c1.id, image='c4.jpg', price=27.00,
              date=datetime.now(),
               name='Adidas Superstar',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s5 = Shoe(category_id=c1.id, image='m1.jpg', price=15.00,
              date=datetime.now(),
               name='Adidas Superstar',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s6 = Shoe(category_id=c1.id, image='m2.jpg', price=18.00,
              date=datetime.now(),
               name='Nike Zoom-2',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s7 = Shoe(category_id=c1.id, image='m3.jpg', price=20.00,
              date=datetime.now(),
               name='Nike Bounce',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')



    s8 = Shoe(category_id=c1.id, image='m4.jpg', price=21.00,
              date=datetime.now(),
               name='Asics Gel Pro',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s9 = Shoe(category_id=c2.id, image='h1.jpg', price=65.00,
              date=datetime.now(),
               name='Hush Puppies Womens Lindera Sandals Heels',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s10 = Shoe(category_id=c2.id, image='h2.jpg', price=40.00,
              date=datetime.now(),
               name='Django & Juliette Women Saritas Heels',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s11 = Shoe(category_id=c2.id, image='h3.jpg', price=25.00,
              date=datetime.now(),
               name='Hush Puppies Hailie ADC heels',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s12 = Shoe(category_id=c2.id, image='h4.jpg', price=30.00,
              date=datetime.now(),
               name='Jimmy Choo- Anouk heels',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s13 = Shoe(category_id=c2.id, image='s1.jpg', price=30.00,
              date=datetime.now(),
               name='Asics-Jump 2',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s14 = Shoe(category_id=c2.id, image='s2.jpg', price=29.00,
              date=datetime.now(),
               name='Nike Ultraboost',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s15 = Shoe(category_id=c2.id, image='s3.jpg', price=35.00,
              date=datetime.now(),
               name='Adidas Adipro',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')



    s16 = Shoe(category_id=c2.id, image='s4.jpg', price=14.00,
              date=datetime.now(),
               name='Reebok Energylux',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')


    s17 = Shoe(category_id=c3.id, image='k1.jpg', price=15.00,
              date=datetime.now(),
               name='Asics Duramo-2',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s18 = Shoe(category_id=c3.id, image='k2.jpg', price=14.00,
              date=datetime.now(),
               name='Adidas Contend-5',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s19 = Shoe(category_id=c3.id, image='k3.jpg', price=16.00,
              date=datetime.now(),
               name='Adidas Nitro',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')
        
    s20 = Shoe(category_id=c3.id, image='k4.jpg', price=18.00,
              date=datetime.now(),
               name='Asics Excite-P6',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ') 

    s21 = Shoe(category_id=c4.id, image='m1.jpg', price=15.00,
              date=datetime.now(),
               name='Adidas Superstar',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s22 = Shoe(category_id=c4.id, image='m2.jpg', price=18.00,
              date=datetime.now(),
               name='Nike Zoom-2',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s23 = Shoe(category_id=c4.id, image='m3.jpg', price=20.00,
              date=datetime.now(),
               name='Nike Bounce',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s24 = Shoe(category_id=c4.id, image='m4.jpg', price=21.00,
              date=datetime.now(),
               name='Asics Gel Pro',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s25 = Shoe(category_id=c5.id, image='c1.jpg', price=22.00,
              date=datetime.now(),
               name='New Balance S-20',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s26 = Shoe(category_id=c5.id, image='c2.jpg', price=23.00,
              date=datetime.now(),
               name='Lacoste-Pegasus',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s27 = Shoe(category_id=c5.id, image='c3.jpg', price=25.00,
              date=datetime.now(),
               name='Hush Puppies-HP30',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s28 = Shoe(category_id=c5.id, image='c4.jpg', price=27.00,
              date=datetime.now(),
               name='Adidas Superstar',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s29 = Shoe(category_id=c6.id, image='h1.jpg', price=65.00,
              date=datetime.now(),
               name='Hush Puppies Womens Lindera Sandals Heels',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s30 = Shoe(category_id=c6.id, image='h2.jpg', price=40.00,
              date=datetime.now(),
               name='Django & Juliette Women Saritas Heels',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')      

    s31 = Shoe(category_id=c6.id, image='h3.jpg', price=25.00,
              date=datetime.now(),
               name='Hush Puppies Hailie ADC heels',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s32 = Shoe(category_id=c6.id, image='h4.jpg', price=30.00,
              date=datetime.now(),
               name='Jimmy Choo- Anouk heels',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s33 = Shoe(category_id=c7.id, image='s1.jpg', price=30.00,
              date=datetime.now(),
               name='Asics-Jump 2',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s34 = Shoe(category_id=c7.id, image='s2.jpg', price=29.00,
              date=datetime.now(),
               name='Nike Ultraboost',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')  

    s35 = Shoe(category_id=c7.id, image='s3.jpg', price=35.00,
              date=datetime.now(),
               name='Adidas Adipro',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')

    s36 = Shoe(category_id=c7.id, image='s4.jpg', price=14.00,
              date=datetime.now(),
               name='Reebok Energylux',
               description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus libero sit amet placerat blandit. ')
                     
    try:
        db.session.add(s1)
        db.session.add(s2)
        db.session.add(s3)
        db.session.add(s4)
        db.session.add(s5)
        db.session.add(s6)
        db.session.add(s7)
        db.session.add(s8)
        db.session.add(s9)
        db.session.add(s10)
        db.session.add(s11)
        db.session.add(s12)
        db.session.add(s13)
        db.session.add(s14)
        db.session.add(s15)
        db.session.add(s16)
        db.session.add(s17)
        db.session.add(s18)
        db.session.add(s19)
        db.session.add(s20)
        db.session.add(s21)
        db.session.add(s22)
        db.session.add(s23)
        db.session.add(s24)
        db.session.add(s25)
        db.session.add(s26)
        db.session.add(s27)
        db.session.add(s28)
        db.session.add(s29)
        db.session.add(s30)
        db.session.add(s31)
        db.session.add(s32)
        db.session.add(s33)
        db.session.add(s34)
        db.session.add(s35)
        db.session.add(s36)


        db.session.commit()
    except:
        return 'There was an issue adding a book in dbseed function'

    return 'DATA LOADED'
