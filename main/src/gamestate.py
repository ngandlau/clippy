from dataclasses import dataclass

from main.src.clippy import Clippy


@dataclass
class Gamestate:
    player: Clippy = None
    bot: Clippy = None
    is_finished: bool = False
