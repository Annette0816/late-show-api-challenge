from models import db
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    guest1 = Guest(name="John Doe", occupation="Actor")
    guest2 = Guest(name="Jane Smith", occupation="Singer")

    episode1 = Episode(date="2025-01-01", number=1)
    episode2 = Episode(date="2025-01-02", number=2)

    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode2)

    db.session.add_all([guest1, guest2, episode1, episode2, appearance1, appearance2])
    db.session.commit()
    print("Seed data created.")
