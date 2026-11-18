from .display import Display

def init(*, display: Display) -> None:
    raise NotImplementedError

def update() -> None:
    raise NotImplementedError

def draw() -> None:
    raise NotImplementedError
