from app import App
from console_io import ConsoleIO
from repositories.user_repository import UserRepository
from services.user_service import UserService


def main():
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    console_io = ConsoleIO()
    app = App(user_service, console_io)

    app.run()


if __name__ == "__main__":
    main()
