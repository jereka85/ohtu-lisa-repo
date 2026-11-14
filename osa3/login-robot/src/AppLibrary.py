from app import App
from repositories.user_repository import UserRepository
from services.user_service import UserService
from stub_io import StubIO


class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._user_repository = UserRepository()
        self._user_service = UserService(self._user_repository)

        self._app = App(
            self._user_service,
            self._io
        )

    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    def create_user(self, username, password):
        self._user_service.create_user(username, password)
        self._io.write("New user registered")

#    def create_wrong_user(self, username, password, value):
#        self._user_service.create_user(username, password)
#        return output_should_contain(self, value)
