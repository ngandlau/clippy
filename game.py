import random
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
        self.reporter.report_message("!!!! WELCOME TO THE JUNGLE !!!!!")
        self.initialize_gamestate(self.state)
        reporter.report_game_state(state)

        while not self.state.is_finished:
            player_action = self.input_processor.get_user_input("Choose Action [Draw, Attack]: ")
            self.execute_player_action(player_action, self.state)
            self.reporter.report_action(self.state.player, self.state.bot, player_action)
            self.check_game_finished(self.state)
            reporter.report_game_state(self.state)

            bot_action = self.draw_bot_action()

            # don't switch these 2 lines. 
            self.reporter.report_action(self.state.bot, self.state.player, player_action)
            self.execute_bot_action(bot_action, self.state)

            self.check_game_finished(self.state)
            reporter.report_game_state(self.state)

        reporter.report_message("Game finished")

    def initialize_gamestate(self, state):
        state.player, state.bot = Clippy("Gormsen"), Clippy("Bot")
        lootbox_player, lootbox_bot = Lootbox(), Lootbox()
        state.player.equip_weapon(lootbox_player.draw_random_weapon())
        state.bot.equip_weapon(lootbox_bot.draw_random_weapon())

    def execute_player_action(self, player_action, state):
        if Action.ATTACK == player_action:
            state.player.attack(state.bot)
        elif Action.DRAW == player_action:
            lootbox = Lootbox()
            state.player.equip_weapon(lootbox.draw_random_weapon())
        else:
            pass

    def check_game_finished(self, state):
        if state.player.life <= 0 or state.bot.life <= 0:
            state.is_finished = True

    def draw_bot_action(self):
        return random.choice([action for action in Action])

    def execute_bot_action(self, bot_action, state):
        if Action.ATTACK == bot_action:
            state.bot.attack(state.player)
        elif Action.DRAW == bot_action:
            lootbox = Lootbox()
            state.bot.equip_weapon(lootbox.draw_random_weapon())
        else:
            pass


if __name__ == '__main__':
    reporter = TerminalReporter()
    state = Gamestate()
    processor = TerminalInputProcessor()

    game = Game(reporter, state, processor)
    game.start()
