
class User:
    def __init__(self, name, email, level, weight, height):
        
        self.name = name
        self.email = email
        self.goals = []
        self.level = level
        self.custom_workouts = []
        self.unit_of_weight = "LBS"  # Can be LBS or KG
        self.unit_of_height = "FT"   # Can be ft. or cm
        self.weight = weight
        self.height = height

