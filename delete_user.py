from session import session
from models import User


def main():
    user = session.query(User).get(142)
    if user is None:
        print("User with id 142 not found")
        return

    session.delete(user)
    session.commit()

    user = session.query(User).get(142)
    if user is None:
        print("User with id 142 deleted")
    else:
        print("User with id 142 not deleted")


if __name__ == "__main__":
    main()
