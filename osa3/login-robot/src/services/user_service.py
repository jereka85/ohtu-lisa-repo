from password_strength import tests
from operator import length_hint
from password_strength import PasswordPolicy
import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        salasanan_vahvuus = PasswordPolicy.from_names(
            length=8,
            nonletters=1
        )

        if not username or not password:
            raise UserInputError("Username and password are required")

        if salasanan_vahvuus.test(password) != []:
            raise UserInputError("Too weak password! There should be at least 8 char and 1 special char.")

        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Username incorrect. There should be at least 3 char.")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
