from flask import Blueprint, request, jsonify
from .models import Hero, Power, HeroPower
from .extensions import db

routes = Blueprint('routes', __name__)

@routes.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    result = [{"id": h.id, "name": h.name, "super_name": h.super_name} for h in heroes]
    return jsonify(result), 200


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


@routes.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "description": p.description
    } for p in powers]), 200

@routes.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    }), 200

@routes.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    if "description" not in data or len(data["description"]) < 20:
        return jsonify({"errors": ["validation errors"]}), 400

    power.description = data["description"]
    db.session.commit()
    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    }), 200


@routes.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get("strength")
    power_id = data.get("power_id")
    hero_id = data.get("hero_id")

    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["validation errors"]}), 400

    power = Power.query.get(power_id)
    hero = Hero.query.get(hero_id)

    if not power or not hero:
        return jsonify({"errors": ["validation errors"]}), 400

    hero_power = HeroPower(strength=strength, hero=hero, power=power)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        "id": hero_power.id,
        "hero_id": hero_power.hero_id,
        "power_id": hero_power.power_id,
        "strength": hero_power.strength,
        "hero": {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        },
        "power": {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
    }), 201
@routes.route('/')
def home():
    return {"message": " Welcome to the Superheroes API!"}, 200
