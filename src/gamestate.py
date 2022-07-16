from clippy import Clippy


@dataclass
class Gamestate:
    player: Clippy = None
    bot: Clippy = None
    is_finished: bool = False

