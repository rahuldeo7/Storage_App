from operator import imod
from flask import Flask, request, abort, jsonify,session
from flask_bcrypt import Bcrypt
from config import ApplicationConfig
from models import db, ClientUser, DevUser

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
bcrypt = Bcrypt(app)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/client-register", methods=["POST"])
def register_user():
    try:
        email = request.json["email"]
        password = request.json["password"]

        user_exists = ClientUser.query.filter_by(email=email).first() is not None

        if user_exists:
            return jsonify({"error": "User already exists"}), 409

        hashed_password = bcrypt.generate_password_hash(password)
        new_user = ClientUser(email=email, password=hashed_password, user_type = "Client")    
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "id": new_user.id,
            "email": new_user.email,
            "user_type" : new_user.user_type
        })
    except Exception as ex:
        print("Exception",ex)


@app.route("/dev-register", methods=["POST"])
def register_dev_user():
    email = request.json["email"]
    password = request.json["password"]
    key = request.json["key"]

    if key == "Passcode":

        user_exists = DevUser.query.filter_by(email=email).first() is not None

        if user_exists:
            return jsonify({"error": "User already exists"}), 409

        hashed_password = bcrypt.generate_password_hash(password)
        new_user = DevUser(email=email, password=hashed_password, user_type = "Developer")
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "id": new_user.id,
            "email": new_user.email,
            "user_type" : new_user.user_type
        })


if __name__ == "main":
    app.run(debug = True)