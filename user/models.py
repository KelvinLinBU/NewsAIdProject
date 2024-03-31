from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
class User:
    def signup(self):
        print(request.form)
        # Create user object
        user = {
            "_id":uuid.uuid4().hex,
            "name":request.form.get('name'),
            "email":request.form.get('email'),
            "password":request.form.get('password'),
        }

        #Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        db.users.insert_one(user)
        return jsonify(user), 200