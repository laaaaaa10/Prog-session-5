class System:
    def __init__(self, state: bool = False) -> None:
        self.state = state

    def read_state(self) -> str:
        return "ON" if self.state else "OFF"

    def change_state(self) -> bool:
        self.state = not self.state
        return self.state
