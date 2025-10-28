from flask import Flask, request
from flask_jwt_extended import JWTManager
from models import (
    db,
    User
)
from flask_migrate import Migrate
from api.schemas import ReviewSchema
from api.views import UserAPI, UserDetailAPI, UserRegisterAPI, AuthLoginAPI

