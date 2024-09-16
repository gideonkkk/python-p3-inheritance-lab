# lib/student.py

from user import User  # Ensure this import exists

class Student(User):  # Inheriting from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Initialize with an empty list

    def learn(self, knowledge):
        self.knowledge.append(knowledge)
