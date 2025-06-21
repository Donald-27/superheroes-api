Superheroes API

This is a small API built using Flask. It keeps track of superheroes and their powers. Each hero can have many powers, and each power can belong to multiple heroes. There is also a connection table called HeroPower that links heroes to powers and includes a strength level (like Strong, Average, or Weak).

What it does:

Lets you get a list of all heroes

Lets you get details of one hero including their powers

Lets you get a list of all powers

Lets you view one power

Lets you update a power description

Lets you create a new hero power link (connects a hero with a power and a strength)

How to set up:

Clone this repo to your machine

Navigate into the folder in your terminal

Create a virtual environment by running:
python3 -m venv .venv

Activate it with:
source .venv/bin/activate

Install all packages:
pip install -r requirements.txt

Set up the database:
flask db init
flask db migrate -m "initial"
flask db upgrade

Seed the database (adds example heroes and powers):
python seed.py

Start the server:
flask run

Once it runs, you can open your browser and go to http://127.0.0.1:5000

Routes:

GET /heroes - shows all heroes
GET /heroes/<id> - shows one hero and their powers
GET /powers - shows all powers
GET /powers/<id> - shows one power
PATCH /powers/<id> - updates a power description (must be at least 20 characters)
POST /hero_powers - creates a new connection between a hero and a power, must include strength, hero_id, and power_id

Strength must be one of these: Strong, Weak, or Average

If you give the wrong values or missing data, it will respond with an error like:
{ "errors": ["validation errors"] }

Sample JSON you can send to create a hero power:

{
"strength": "Average",
"power_id": 2,
"hero_id": 1
}

If it's successful, it will respond with a new hero power plus the hero and power data inside.

This app is for the Phase 4 assessment.
Built with Flask and SQLite.
Simple and meant to be easy to understand.
