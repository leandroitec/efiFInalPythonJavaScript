from flask import Flask, request
from flask_jwt_extended import JWTManager
from models import (
    db,
    Movie,
    Review
)
from flask_migrate import Migrate
from schemas import ReviewSchema
from views import UserAPI, UserDetailAPI, UserRegisterAPI, AuthLoginAPI

app = Flask(__name__)
#cambiar esto si tenes usuario y contraseña, //usuario:contraseña@host:@localhost/pyIIefi_db"
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mysql+pymysql://root:leli@localhost/pppythonEfiFinal"
)
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'cualquier-cosa'

jwt = JWTManager(app)
db.init_app(app)

app.add_url_rule(
    '/users',
    view_func=UserAPI.as_view('users_api'),
    methods=['POST', 'GET']
)
app.add_url_rule(
    '/users/<int:id>',
    view_func=UserDetailAPI.as_view('user_detail_api'),
    methods=['GET', 'PUT', 'PATCH', 'DELETE']
)
app.add_url_rule(
    '/register',
    view_func=UserRegisterAPI.as_view('user_register_api'),
    methods=['POST']
)
app.add_url_rule(
    '/login',
    view_func=AuthLoginAPI.as_view('user_user_api'),
    methods=['POST']
)

@app.route('/reviews')
def reviews():
    reviews = Review.query.all()
    return ReviewSchema(many=True).dump(reviews)

@app.route('/reviews/<int:id>', methods=['GET'])
def review(id):
    review = Review.query.get_or_404(id)
    return ReviewSchema().dump(review)

@app.route('/movies')
def movies():
    movies = Movie.query.all()
    return [
        {
            "title": movie.title,
            "year": movie.year,
            #"genres": movie.genres
        } for movie in movies
    ]


if __name__ == '__main__':
    app.run(debug=True)