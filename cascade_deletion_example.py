from session import session, commit_on_success
from models import Author


@commit_on_success
def main():
    authors = [
        author
        for author in session.query(Author)
        if len(author.articles) > 0
    ]

    if len(authors) == 0:
        print("There are no authors with articles")
        return

    print("Authors with articles: ")
    for author in authors:
        print(author)

    target_author = authors[0]
    print(f"Try to delete author: {target_author}")
    session.delete(target_author)


if __name__ == "__main__":
    main()
