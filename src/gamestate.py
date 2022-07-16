from dataclasses import dataclass

from src.clippy import Clippy


@dataclass
class Gamestate:
    player: Clippy = None
    bot: Clippy = None
    is_finished: bool = False
