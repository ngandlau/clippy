from dataclasses import dataclass

from src.clippy import Clippy


@dataclass
class Game:
    reporter = None
    state = None
    input_processor = None

    def start(self):
        self.reporter.report_message("Hello World")
        self.initialize_gamestate(state)
        while not self.state.is_finished():
            action = self.input_processor.get_user_input()
            self.execute_actions(action, state)
            reporter.report_game_state(state)
        reporter.report_game_state(state)
        reporter.report_message("Game finished")

    def execute_actions(self, action, state):
        pass

    def initialize_gamestate(self, state):
        state.player = Clippy()
        state.bot = Clippy()

class Reporter:
    def report_game_state(self, state):
        pass

    def report_message(self, param):
        pass


@dataclass
class Gamestate():
    player = None
    bot = None

class InputProcessor:
    pass

class ConsoleReporter:
    pass

class ConsoleInputProcessor:
    pass


if __name__ == '__main__':
    reporter = Reporter()
    state = Gamestate()
    processor = InputProcessor()

    game = Game(state, reporter, processor)
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
    
    

