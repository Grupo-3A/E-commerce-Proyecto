import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://admin:1001204488@localhost:5432/e_commerce_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False