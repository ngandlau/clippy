from dataclasses import dataclass

from main.src.action import Action
from main.src.clippy import Clippy
from main.src.gamestate import Gamestate
from main.src.inputprocessor import InputProcessor, TerminalInputProcessor
from main.src.lootbox import Lootbox
from main.src.out.reporter import Reporter, TerminalReporter


@dataclass
class Game:
    reporter: Reporter
    state: Gamestate
    input_processor: InputProcessor

    def start(self):
        self.reporter.report_message("Hello World")
        self.initialize_gamestate(self.state)
        reporter.report_game_state(state)
        while not self.state.is_finished:
            action: Action = self.input_processor.get_user_input("Chose Action [Draw, Attack]: ")
            self.execute_actions(action, state)
            reporter.report_game_state(state)
        reporter.report_game_state(state)
        reporter.report_message("Game finished")

    def initialize_gamestate(self, state):
        state.player, state.bot = Clippy(), Clippy()
        lootbox_player, lootbox_bot = Lootbox(), Lootbox()
        state.player.equip_weapon(lootbox_player.draw_random_weapon())
        state.bot.equip_weapon(lootbox_bot.draw_random_weapon())

    def execute_actions(self, action, state):
        if Action.ATTACK == action:
            state.player.attack(state.bot)
        elif Action.DRAW == action:
            pass
        else:
            pass



if __name__ == '__main__':
    reporter = TerminalReporter()
    state = Gamestate()
    processor = TerminalInputProcessor()

    game = Game(reporter, state, processor)
    game.start()

    """
    == Ablauf == 
    start_game()
    while nobody won:
        report_gamestate()
        play_round()
            get_player_action()
            execute_player_action()
            update_gamestate()           

    == Klassen ==
    * InputProcessor -- prozessiert Spielerinputs
    * Game -- ???
    * GameState -- speichert den aktuellen Spielzustand
    * Player -- ein Clippy
    * Reporter -- GameState veröffentlichen (e.g., in Konsole printen)
    """
