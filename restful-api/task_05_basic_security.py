#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
        "yveline": {
            "username": "yveline",
            "password": generate_password_hash("password"),
            "role": "user"
        },
        "youssoup": {
            "username": "youssoup",
            "password": generate_password_hash("password"),
            "role": "user"
        },
        "jeremy": {
            "username": "jeremy",
            "password": generate_password_hash("password"),
            "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity={
                "username": username,
                "role": user['role']
            })
            return jsonify({
                "access_token": access_token
            })
    return jsonify({
        "error": "Invalid credentials"
    }), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    if user['role'] != "admin":
        return jsonify({
            "error": "Permission denied"
        }), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
