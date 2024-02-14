from typing import Callable, Hashable, Iterable, List, Optional, Tuple, Union

from pygame.surface import Surface

from ._common import ColorValue, FileArg, Literal

# TODO: Figure out a way to type this attribute such that mypy knows it's not
# always defined at runtime
UCS4: Literal[1]

def init() -> None: ...
def quit() -> None: ...
def get_init() -> bool: ...
def get_sdl_ttf_version(linked: bool = True) -> Tuple[int, int, int]: ...
def get_default_font() -> str: ...
def get_fonts() -> List[str]: ...
def match_font(
    name: Union[str, bytes, Iterable[Union[str, bytes]]],
    bold: Hashable = False,
    italic: Hashable = False,
) -> str: ...
def SysFont(
    name: Union[str, bytes, Iterable[Union[str, bytes]], None],
    size: int,
    bold: Hashable = False,
    italic: Hashable = False,
    constructor: Optional[Callable[[Optional[str], int, bool, bool], Font]] = None,
) -> Font: ...

class Font:
    @property
    def name(self) -> str: ...
    @property
    def style_name(self) -> str: ...
    @property
    def bold(self) -> bool: ...
    @bold.setter
    def bold(self, value: bool) -> None: ...
    @property
    def italic(self) -> bool: ...
    @italic.setter
    def italic(self, value: bool) -> None: ...
    @property
    def underline(self) -> bool: ...
    @underline.setter
    def underline(self, value: bool) -> None: ...
    @property
    def strikethrough(self) -> bool: ...
    @strikethrough.setter
    def strikethrough(self, value: bool) -> None: ...
    @property
    def align(self) -> int: ...
    @align.setter
    def align(self, value: int) -> None: ...
    @property
    def point_size(self) -> int: ...
    @point_size.setter
    def point_size(self, value: int) -> None: ...
    def __init__(self, filename: Optional[FileArg] = None, size: int = 20) -> None: ...
    def render(
        self,
        text: Union[str, bytes, None],
        antialias: bool,
        color: ColorValue,
        bgcolor: Optional[ColorValue] = None,
        wraplength: int = 0,
    ) -> Surface: ...
    def size(self, text: Union[str, bytes], /) -> Tuple[int, int]: ...
    def set_underline(self, value: bool, /) -> None: ...
    def get_underline(self) -> bool: ...
    def set_strikethrough(self, value: bool, /) -> None: ...
    def get_strikethrough(self) -> bool: ...
    def set_bold(self, value: bool, /) -> None: ...
    def get_bold(self) -> bool: ...
    def set_italic(self, value: bool, /) -> None: ...
    def metrics(
        self, text: Union[str, bytes], /
    ) -> List[Tuple[int, int, int, int, int]]: ...
    def get_italic(self) -> bool: ...
    def get_linesize(self) -> int: ...
    def get_height(self) -> int: ...
    def get_ascent(self) -> int: ...
    def get_descent(self) -> int: ...
    def set_script(self, script_code: str, /) -> None: ...
    def set_direction(self, direction: int) -> None: ...
    def get_point_size(self) -> int: ...
    def set_point_size(self, val: int, /) -> None: ...
    def set_kerning(self, value: bool, /) -> None: ...

FontType = Font
