# command center for managing app (register custom terminal commands to control app) from the terminal.
from flask.cli import FlaskGroup

from project import app, db, User

# created a new FlaskGroup instance to extend the normal CLI with commands related to the Flask app.
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# seed command for adding sample users to the users table
@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()


if __name__ == "__main__":
    cli()
