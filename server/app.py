from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # ✅ Required for db migrations

from models import db, Animal, Zookeeper, Enclosure

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)  # ✅ This line is required for flask db commands

@app.route('/animal/<int:id>')
def animal(id):
    animal = Animal.query.get(id)

    if animal is None:
        return "<h1>Animal not found</h1>"

    return f"""
        <ul>Name: {animal.name}</ul>
        <ul>Species: {animal.species}</ul>
        <ul>Zookeeper: {animal.zookeeper.name}</ul>
        <ul>Enclosure: {animal.enclosure.environment}</ul>
    """



@app.route('/zookeeper/<int:id>')
def zookeeper(id):
    zookeeper = Zookeeper.query.get(id)

    if zookeeper is None:
        return "<h1>Zookeeper not found</h1>"

    animals = "".join([f"<li>{animal.name} ({animal.species})</li>" for animal in zookeeper.animals])

    return f"""
        <ul>Name: {zookeeper.name}</ul>
        <ul>Birthday: {zookeeper.birthday}</ul>
        <ul>Animals:
            <ul>
                {animals}
            </ul>
        </ul>
    """


@app.route('/enclosure/<int:id>')
def enclosure(id):
    enclosure = Enclosure.query.get(id)

    if enclosure is None:
        return "<h1>Enclosure not found</h1>"

    animals = "".join([f"<li>{animal.name} ({animal.species})</li>" for animal in enclosure.animals])

    return f"""
        <ul>Environment: {enclosure.environment}</ul>
        <ul>Open to Visitors: {enclosure.open_to_visitors}</ul>
        <ul>Animals:
            <ul>
                {animals}
            </ul>
        </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)
