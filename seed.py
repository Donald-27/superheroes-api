# seed.py

from app import create_app
from app.extensions import db
from app.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    
    db.session.query(HeroPower).delete()
    db.session.query(Hero).delete()
    db.session.query(Power).delete()

    hero1 = Hero(name="Superman", super_name="Clark Kent")
    hero2 = Hero(name="Batman", super_name="Bruce Wayne")

    power1 = Power(name="Flight", description="Fly through the sky at fast speeds.")
    power2 = Power(name="Strength", description="Lift very heavy things easily.")

    hp1 = HeroPower(hero=hero1, power=power1, strength="Strong")
    hp2 = HeroPower(hero=hero2, power=power2, strength="Average")

    db.session.add_all([hero1, hero2, power1, power2, hp1, hp2])
    db.session.commit()

    print("Database seeded successfully.")
