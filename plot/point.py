from enum import StrEnum


class BasePoint:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class LandPoint(BasePoint):
    pass


class HandPlacementEnum(StrEnum):
    FRONT = "front"
    BACK = "back"


class Porter(BasePoint):
    def __init__(self, x: float, y: float, hand_placement: HandPlacementEnum):
        super().__init__(x=x, y=y)
        self.hand_placement = hand_placement


Porter(x=1, y=2, hand_placement=HandPlacementEnum.FRONT)