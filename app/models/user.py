from flask import current_app

class UserModel:
    @staticmethod
    def find_by_id_user(id_user):
        """Trouver un utilisateur par son nom d'utilisateur."""
        user = current_app.db.users.find_one({"_id": id_user})
        return user
    
    def find_all_user():
        """Trouver tout les utilisateurs."""
        users = current_app.db.users.find()
        return users

    @staticmethod
    def create_user(data):
        """Créer un nouvel utilisateur."""
        result = current_app.db.users.insert_one(data)
        return result.inserted_id