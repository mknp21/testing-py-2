from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///testdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    example_game = Game("Pictionary", "draw pictures and guess")
    # df = Department(dept_code='fin', dept='Finance', phone='555-1000')
    # dl = Department(dept_code='legal', dept='Legal', phone='555-2222')
    # dm = Department(dept_code='mktg', dept='Marketing', phone='555-9999')

    # leonard = Employee(name='Leonard', dept=dl)
    # liz = Employee(name='Liz', dept=dl)
    # maggie = Employee(name='Maggie', dept=dm)
    # nadine = Employee(name='Nadine')



if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
