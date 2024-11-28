# app/routes/user_routes.py
from flask import Blueprint, jsonify, render_template, request
from app.models.user import UserModel

# Définir le blueprint
user_routes = Blueprint('user', __name__)

@user_routes.route('/users', methods=['GET'])
def get_users():
    """Récupérer les informations d'un utilisateur."""
    users = UserModel.find_all_user()
    if users:
        return jsonify(users)
        # return jsonify(user), 200
        return render_template("profile.html", users=users)
    return jsonify({"error": "User not found"}), 404

@user_routes.route('/user/<id_user>', methods=['GET'])
def get_user(id_user):
    """Récupérer les informations d'un utilisateur."""
    user = UserModel.find_by_id_user(id_user)
    if user:
        # return jsonify(user), 200
        return render_template("profile.html", user=user)
    return jsonify({"error": "User not found"}), 404
