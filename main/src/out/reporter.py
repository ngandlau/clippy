from main.src.action import Action

class Reporter:
    def report_game_state(self, state):
        pass

    def report_message(self, msg):
        pass


class TerminalReporter(Reporter):
    def report_game_state(self, state):
        txt = f"""
    o-------------------------------------------------------------------------------o
    | Player - Life: {state.player.life} | Weapon: {state.player.weapon.get_name()} 
    | Comptr - Life: {state.bot.life} | Weapon: {state.bot.weapon.get_name()}       
    o-------------------------------------------------------------------------------o
        """
        print(txt)

    def report_message(self, msg: str):
        print(msg)

    def report_action(self, player1, player2, action):
        pass
        # if Action.ATTACK == action:
        #     print(f'{player1.name} attacked {player2.name} with a {player1.weapon.get_name()}')
        # elif Action.DRAW == action:
        #     print(f'{player1.name} has drawn a new weapon: {player1.weapon.get_name()}')
        # else:
        #     print(f'Wrong Action')



