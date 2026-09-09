class Sensor:
    def __init__(
        self,
        name: str,
        unit: str,
        value: float = 0.0,
    ) -> None:
        self.name = name
        self.unit = unit
        self.value = value

    def read(self) -> float:
        return self.value

    def read_value(self) -> float:
        self.value = 22.3
        return self.value

    def set_value(self, value: float) -> None:
        self.value = value


