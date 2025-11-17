from contextlib import AbstractContextManager
import contextvars


_current_uow = contextvars.ContextVar("_current_uow", default=None)

class UnitOfWork(AbstractContextManager):
    """Just a class to contains repository"""
    def __init__(self, session):
        self.session = session
        self._repos = {}

    def __enter__(self):
        # On enregistre le UnitOfWork courant dans le contexte
        self._token = _current_uow.set(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        _current_uow.reset(self._token)

    def get_repo(self, repo_cls):
        if repo_cls not in self._repos:
            model_cls = getattr(repo_cls, "__args__", [None])[0]
            self._repos[repo_cls] = repo_cls(self.session, model_cls)
        return self._repos[repo_cls]
