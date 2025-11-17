from typing import Generic, TypeVar, Type

from sqlalchemy.orm import Session


T = TypeVar("T")


class GenericRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def _all_session_objects(self):
        for obj in list(self.session.identity_map.values()) + list(self.session.new):
            if isinstance(obj, self.model):
                yield obj

    def get(self, **filters) -> T | None:
        for obj in self._all_session_objects():
            if all(getattr(obj, k) == v for k, v in filters.items()):
                return obj

        return self.session.query(self.model).filter_by(**filters).first()

    def get_all(self, **filters) -> list[T]:
        results = []

        for obj in self._all_session_objects():
            if not filters or all(getattr(obj, k) == v for k, v in filters.items()):
                results.append(obj)

        query = self.session.query(self.model)
        if filters:
            query = query.filter_by(**filters)
        query_results = query.all()

        session_ids = {id(obj) for obj in results}
        for obj in query_results:
            if id(obj) not in session_ids:
                results.append(obj)

        return results

    def exists(self, **filters) -> bool:
        for obj in self._all_session_objects():
            if all(getattr(obj, k) == v for k, v in filters.items()):
                return True
        return self.session.query(
            self.session.query(self.model).filter_by(**filters).exists()
        ).scalar()
