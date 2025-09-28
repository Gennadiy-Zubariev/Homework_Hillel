from flask import Blueprint, render_template
from models import Media

main = Blueprint('main', __name__)

@main.route('/')
def index():
    movies = Media.query.filter_by(type='movie').order_by(Media.created_at.desc()).all()
    series = Media.query.filter_by(type='series').order_by(Media.created_at.desc()).all()
    return render_template('index.html', movies=movies, series=series)

@main.route('/about')
def about():
    return render_template('about.html')