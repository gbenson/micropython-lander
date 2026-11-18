from ... import lander
from ...display import Display as _Display


class Display(_Display):
    pass


def main() -> None:
    lander.init(display=Display())
    run(update)  # type: ignore[name-defined]  # noqa: F821


def update() -> None:
    lander.update()
    lander.draw()
