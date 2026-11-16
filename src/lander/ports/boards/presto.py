from presto import Presto

from ... import lander
from ..picographics import Display


def main() -> None:
    presto = Presto(full_res=True, palette=True)
    presto.clear()
    lander.init(display=Display(presto.display))
    while True:
        lander.update()
        lander.draw()
        presto.update()
