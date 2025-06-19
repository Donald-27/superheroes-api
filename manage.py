from app import create_app
from app.extensions import db
from flask_migrate import Migrate

# Step 1: Create the Flask app using the factory function
app = create_app()

# Step 2: Set up Flask-Migrate to handle database migrations
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
