import os
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
db = SQLAlchemy(app)

# Stripe setup
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
YOUR_DOMAIN = "http://127.0.0.1:5000"

#  MODELS 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # in cents
    image_url = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()
    # Add demo products if empty
    if Product.query.count() == 0:
        db.session.add_all([
            Product(name="AI T-shirt", price=2500, image_url="https://picsum.photos/200?1"),
            Product(name="Raspberry Pi Robot", price=9500, image_url="https://picsum.photos/200?2"),
            Product(name="Flask Mug", price=1800, image_url="https://picsum.photos/200?3")
        ])
        db.session.commit()

# LOGIN MANAGER 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ROUTES
@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)
        if User.query.filter_by(email=email).first():
            flash("Email already exists.")
            return redirect(url_for("register"))
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("index"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Invalid credentials")
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

# CART
@app.route("/add_to_cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    cart = session.get("cart", [])
    cart.append(product_id)
    session["cart"] = cart
    flash("Added to cart!")
    return redirect(url_for("index"))

@app.route("/cart")
@login_required
def cart():
    cart = session.get("cart", [])
    items = Product.query.filter(Product.id.in_(cart)).all() if cart else []
    total = sum(p.price for p in items)
    return render_template("cart.html", items=items, total=total)

#  STRIPE CHECKOUT
@app.route("/create-checkout-session", methods=["POST"])
@login_required
def create_checkout_session():
    cart = session.get("cart", [])
    if not cart:
        flash("Your cart is empty!")
        return redirect(url_for("index"))

    items = Product.query.filter(Product.id.in_(cart)).all()
    line_items = [{
        "price_data": {
            "currency": "usd",
            "product_data": {"name": p.name},
            "unit_amount": p.price,
        },
        "quantity": 1,
    } for p in items]

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=YOUR_DOMAIN + "/success",
        cancel_url=YOUR_DOMAIN + "/cart",
    )
    return redirect(checkout_session.url, code=303)

@app.route("/success")
def success():
    session["cart"] = []
    return render_template("checkout.html")

#  RUN
if __name__ == "__main__":
    app.run(debug=True)
