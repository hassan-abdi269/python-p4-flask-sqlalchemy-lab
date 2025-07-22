from models import db, Animal, Zookeeper, Enclosure
from app import app

with app.app_context():
    print("🧹 Clearing db...")
    Animal.query.delete()
    Zookeeper.query.delete()
    Enclosure.query.delete()

    print("🌱 Seeding data...")

    zk1 = Zookeeper(name="Dylan Taylor", birthday="1990-05-15")
    zk2 = Zookeeper(name="Stephanie Contreras", birthday="1996-09-20")

    en1 = Enclosure(environment="trees", open_to_visitors=True)
    en2 = Enclosure(environment="pond", open_to_visitors=False)

    a1 = Animal(name="Logan", species="Snake", zookeeper=zk1, enclosure=en1)
    a2 = Animal(name="Max", species="Otter", zookeeper=zk2, enclosure=en2)

    db.session.add_all([zk1, zk2, en1, en2, a1, a2])
    db.session.commit()

    print("✅ Done!")
