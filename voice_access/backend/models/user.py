# user model definition
from datetime import datetime

class User:
    def __init__(self, name, phone, gender, height=None, weight=None):
        self.name = name
        self.phone = phone
        self.gender = gender
        self.height = height
        self.weight = weight

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
        }