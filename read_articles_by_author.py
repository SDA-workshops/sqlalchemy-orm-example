from models import Author
from session import session


def main():
    login = input("Input author login: ")

    author = session.query(Author).filter(Author.login == login).first()
    if author is None:
        print(f"Author with login {login} not found")
        return

    print(f"The list of articles of {author}:")
    for article in author.articles:
        print(f"- {article}")


if __name__ == "__main__":
    main()
