from attack_graph.node import Node


class Edge:
    def __init__(
        self, src: Node, dst: Node, label, reasons: list[str] = None, cmd: str = ""
    ):
        self.src: Node = src
        self.dst: Node = dst
        self.label: str = label
        self.command: str = cmd
        self.reasons: list[str] = reasons

    def __str__(self):
        return f"{self.src} -> {self.dst} {self.label:10} {self.reasons} {self.command}"  # noqa E231

    def __eq__(self, other) -> bool:
        # print(f"Comparison\n{str(self)}\n{str(other)}\n===========")
        return (
            self.src.user == other.src.user
            and self.dst.user == other.dst.user
            and self.src.machine == other.src.machine
            and self.dst.machine == other.dst.machine
            and self.label == other.label
            and str(self.reasons) == str(other.reasons)
            and self.command == other.command
        )

    def __repr__(self):
        return f"Edge(src={self.src}, dst={self.dst}, label={self.label}, reasons={self.reasons}, command={self.command})"
