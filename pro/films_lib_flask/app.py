from flask import Flask
from db_config import init_db
from routes.main_routes import main
from routes.movie_routes import media_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['OMDB_API_KEY'] = 'ebb4fbe7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_diary.db'
init_db(app)

app.register_blueprint(main)
app.register_blueprint(media_bp)

if __name__ == '__main__':
    app.run(debug=True)