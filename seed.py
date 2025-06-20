from app import create_app
from app.extensions import db
from app.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
  
    db.drop_all()
    db.create_all()

    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    h3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")

    p1 = Power(name="super strength", description="gives the wielder super-human strengths")
    p2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    p3 = Power(name="super human senses", description="allows the wielder to use her senses at a super-human level")


    hp1 = HeroPower(strength="Strong", hero=h1, power=p2)
    hp2 = HeroPower(strength="Average", hero=h1, power=p1)
    hp3 = HeroPower(strength="Weak", hero=h2, power=p3)


    db.session.add_all([h1, h2, h3, p1, p2, p3, hp1, hp2, hp3])
    db.session.commit()

    print("Seeded database successfully!")
