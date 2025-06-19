from flask import Blueprint, request, jsonify
from .models import Hero, Power, HeroPower
from .extensions import db

routes = Blueprint('routes', __name__)

# a. GET /heroes
@routes.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    result = [{"id": h.id, "name": h.name, "super_name": h.super_name} for h in heroes]
    return jsonify(result), 200


# b. GET /heroes/<int:id>
@routes.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [
            {
                "id": hp.id,
                "strength": hp.strength,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "power": {
                    "id": hp.power.id,
                    "name": hp.power.name,
                    "description": hp.power.description
                }
            } for hp in hero.hero_powers
        ]
    }), 200


# c. GET /powers
@routes.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "description": p.description
    } for p in powers]), 200


