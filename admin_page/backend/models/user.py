# user model definition
from datetime import datetime

class User:
    def __init__(self, name, phone, birthdate, gender, height=None, weight=None):
        self.name = name
        self.phone = phone
        self.birthdate = birthdate
        self.gender = gender
        self.height = height
        self.weight = weight

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
        }