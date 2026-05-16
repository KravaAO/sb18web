from flask import Flask, render_template, request
from models import User, Book, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['get', 'post'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html')


@app.route('/users')
def get_all_users():
    users_list = User.query.all()
    return render_template('users.html', users_list=users_list)

@app.route('/users/<id: int>')
def user_detail(pk):
    user = User.query.get(pk)
    return render_template('users.html')


@app.route('/book_create', methods=['post', 'get'])
def book_create():
    if request.method ==  'POST':
        description = request.form.get('description')
        name = request.form.get('name')
        book = Book(name=name, description=description)
        db.session.add(book)
        db.session.commit()
    return render_template('book_create.html')


@app.route('/books')
def books():
    books_list = Book.query.all()
    return render_template('books.html', books=books_list)


with app.app_context():
    db.create_all()

app.run(debug=True)
