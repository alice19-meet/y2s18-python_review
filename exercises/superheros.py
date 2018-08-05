# Write your solutions for 1.5 here!
class Superheroes:
    def __init__(self, name,superpower, strength):
        self.name = name
        self.superpower = superpower
        self.strength= strength
    
    def write(self):
          print(self.name, self.strength)
    
    def save_civilian(self, work):
        self.strength= self.strength-work
        




