from backend.database.session import Base
from backend.database.session import engine

from backend.models.user import User
from backend.models.case import Case


def init_db():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":

    init_db()
