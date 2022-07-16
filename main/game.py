from dataclasses import dataclass

@dataclass
class Game:
    reporter = None
    state = None
    processor = None

    def start():
        self.reporter.report("Hello World")
        while not self.state.is_finished():
            pass
            

class Reporter:
    pass

class Gamestate:
    pass

class InputProcessor:
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
    
    

