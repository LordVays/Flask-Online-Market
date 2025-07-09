from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Product, Order
from . import db, login_manager

bp = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/')
def index():
    featured_products = Product.query.limit(4).all()
    return render_template('index.html', products=featured_products)

@bp.route('/products')
def products():
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)

@bp.route('/profile')
@login_required
def profile():
    user_orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', user=current_user, orders=user_orders)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('main.profile'))
        else:
            flash('Неверное имя пользователя или пароль', 'danger')
    
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        
        if existing_user:
            flash('Имя пользователя или email уже заняты', 'danger')
            return redirect(url_for('main.register'))
        
        hashed_password = generate_password_hash(password, method='scrypt')
        new_user = User(username=username, email=email, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Регистрация прошла успешно! Теперь вы можете войти.', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('main.index'))

@bp.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    
    if 'cart' not in session:
        session['cart'] = []
    
    cart = session['cart']
    product_in_cart = next((item for item in cart if item['id'] == product.id), None)
    
    if product_in_cart:
        product_in_cart['quantity'] += 1
    else:
        cart.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1
        })
    
    session['cart'] = cart
    flash(f'{product.name} добавлен в корзину', 'success')
    return redirect(url_for('main.products'))

@bp.route('/checkout')
@login_required
def checkout():
    if 'cart' not in session or not session['cart']:
        flash('Ваша корзина пуста', 'warning')
        return redirect(url_for('main.products'))
    
    cart = session['cart']
    
    for item in cart:
        order = Order(
            user_id=current_user.id,
            product_id=item['id'],
            quantity=item['quantity']
        )
        db.session.add(order)
    
    db.session.commit()
    session.pop('cart', None)
    
    flash('Заказ оформлен успешно!', 'success')
    return redirect(url_for('main.profile'))