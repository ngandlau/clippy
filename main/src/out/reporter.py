class Reporter:
    def report_game_state(self, state):
        pass

    def report_message(self, msg):
        pass


class TerminalReporter(Reporter):
    def report_game_state(self, state):
        txt = f"""
        Player - Life: {state.player.life} | Weapon: {state.player.weapon.get_name()}
        Comptr - Life: {state.bot.life} | Weapon: {state.bot.weapon.get_name()}
        """
        print(txt)

    def report_message(self, msg: str):
        print(msg)
