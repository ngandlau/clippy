class Reporter:
    def report_game_state(self, state):
        pass

    def report_message(self, msg):
        pass


class TerminalReporter(Reporter):
    def report_game_state(self, state):
        txt = f"""
        Lifepoints
            Player: {state.player.life}
            Comptr: {state.bot.life}
        """
        print(txt)

    def report_message(self, msg: str):
        print(msg)
