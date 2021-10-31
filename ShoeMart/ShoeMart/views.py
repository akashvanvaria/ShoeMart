from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Shoe, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db


bp = Blueprint('main', __name__)

# route to index page
@bp.route('/')
def index():
    categories = Category.query.filter((Category.name== 'Men') | (Category.name== 'Women') | (Category.name== 'Kids'))
    return render_template('index.html', categories=categories)

@bp.route('/Account', methods=['POST','GET'])
def Account():
    return render_template('Account.html')  

# Search for products

@bp.route('/search/', methods=['POST','GET'])
def search():
    search = request.args.get('search')
    print(search)
    search = '%{}%'.format(search)
    shoes = Shoe.query.filter(Shoe.name.like(search)).all()
    return render_template('search.html', shoes=shoes) 

# route to men page

@bp.route('/men/<int:id>/')
def Men(id):
    shoes = Shoe.query.filter(Shoe.category_id== id)
    return render_template('Men.html', shoes = shoes)

# route to women page

@bp.route('/women/<int:id>/')
def Women(id):
    shoes = Shoe.query.filter(Shoe.category_id== id)
    return render_template('Women.html', shoes = shoes)

# route to kids page

@bp.route('/kids/<int:id>/')
def Kids(id):
    shoes = Shoe.query.filter(Shoe.category_id== id)
    return render_template('Kids.html', shoes = shoes)

# route to women's sports category

@bp.route('/sports_women/')
def sports_women():
    shoes = Shoe.query.filter((Shoe.category_id== '7'))
    return render_template('sports_women.html', shoes=shoes)

# route to men's sports category

@bp.route('/sports_men/')
def sports_men():
    shoes = Shoe.query.filter((Shoe.category_id== '4'))
    return render_template('sports_men.html', shoes=shoes)  

# route to women's heels

@bp.route('/heels_women/')
def heels_women():
    shoes = Shoe.query.filter((Shoe.category_id== '6'))
    return render_template('heels_women.html', shoes=shoes)

# route to men's casual category

@bp.route('/casual_men/')
def casual_men():
    shoes = Shoe.query.filter((Shoe.category_id== '5'))
    return render_template('casual_men.html', shoes=shoes)  

# adding shoes to cart


@bp.route('/order', methods=['POST','GET'])
def order():
    shoe_id = request.values.get('shoe_id')


    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for shoe in order.shoes:
            totalprice = totalprice + shoe.price
    
    # are we adding an item?
    if shoe_id is not None and order is not None:
        shoe = Shoe.query.get(shoe_id)
        if shoe not in order.shoes:
            try:
                order.shoes.append(shoe)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))
    
    return render_template('cart.html', orders = order, totalprice = totalprice)


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        shoe_to_delete = Shoe.query.get(id)
        try:
            order.shoes.remove(shoe_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items have been deleted from the cart')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for shoe in order.shoes:
                totalcost = totalcost + shoe.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thanks for placing your order, your invoice has been mailed to your email-address.')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form = form)
