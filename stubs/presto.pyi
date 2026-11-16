from picographics import PicoGraphics

class Presto:
    display: PicoGraphics
    def __init__(
            self,
            *,
            full_res: bool = False,
            palette: bool = False,
    ) -> None: ...
    def clear(self) -> None: ...
    def update(self) -> None: ...
