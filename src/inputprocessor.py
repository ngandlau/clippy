from src.action import Action


class InputProcessor:
    def get_user_input(self, msg: str):
        pass


class TerminalInputProcessor(InputProcessor):

    def get_user_input(self, msg: str) -> Action:
        user_input = input(msg)
        if user_input == "Attack":
            return Action.ATTACK
        elif user_input == "Draw":
            return Action.DRAW
        else:
            return Action.INVALID
