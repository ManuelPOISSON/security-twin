class Node:
    def __init__(self, m: str, u: str, reasons: list[str] = None):
        self.machine: str = m
        self.user: str = u
        if reasons is None:
            reasons = []
        self.reasons: list[str] = reasons

    def __repr__(self):
        if self.user.startswith("S-1-5-21-"):
            return f"({self.machine},..{'-'.join(self.user.split('-')[-2:])},{self.reasons})"  # noqa E231
        return f"({self.machine},{self.user},{self.reasons})"  # noqa E231

    def __str__(self):
        if self.user.startswith("S-1-5-21-"):
            return (
                f"({self.machine},..{'-'.join(self.user.split('-')[-2:])})"  # noqa E231
            )
        return f"({self.machine},{self.user})"  # noqa E231

    def __eq__(self, other) -> bool:
        return (
            self.machine == other.machine
            and self.user == other.user
            and str(self.reasons) == str(other.reasons)
        )

    def __hash__(self):
        return hash((self.machine, self.user))
