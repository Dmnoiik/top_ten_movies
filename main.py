from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from forms import EditForm, AddForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit_movie():
    edit = EditForm()
    if request.method == 'POST':
        new_rating = float(request.form['rating_field'])
        new_review = request.form['review_field']
        print(new_rating)
        with app.app_context():
            current_movie = db.get_or_404(Movie, request.args['id'])
            current_movie.rating = new_rating
            current_movie.review = new_review
            db.session.commit()
        return redirect('/')
    if request.method == "GET":
        current_id = request.args['id']
        return render_template('edit.html', form=edit, movie_id=current_id)

@app.route('/delete', methods=['GET'])
def delete_movie():
    if request.method == "GET":
        with app.app_context():
            movie_to_delete = db.get_or_404(Movie, request.args['id'])
            db.session.delete(movie_to_delete)
            db.session.commit()
        return redirect('/')

@app.route('/add', methods=["GET", "POST"])
def add_movie():
    add_form = AddForm()
    if request.method == "POST":
        movie_title = request.form['title']
        response = requests.get('')
        return render_template('select.html')
    if request.method == "GET":
        return render_template('add.html', form=add_form)

if __name__ == '__main__':
    app.run(debug=True)
