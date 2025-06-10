from sqlalchemy.orm import Session


class Repository[T]:
    def __init__(self, session: Session, table: type[T]):
        self.session = session
        self.table = table

    def get_all(self) -> list[T]:
        return self.session.query(self.table).all()

    def commit(self) -> None:
        self.session.commit()
