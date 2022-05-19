from textual.message import Message, MessageTarget


class Keystroke(Message, bubble=True):
    def __init__(self, sender: MessageTarget, key: str) -> None:
        super().__init__(sender)
        self.key = key


class MenuOptionChange(Message, bubble=True):
    def __init__(self, sender: MessageTarget, option: str) -> None:
        super().__init__(sender)
        self.option = option


class ChangeStatus(Message, bubble=True):
    def __init__(self, sender: MessageTarget, status: str) -> None:
        super().__init__(sender)
        self.status = status


class ShowMessage(Message, bubble=True):
    def __init__(self, sender: MessageTarget, message: str) -> None:
        super().__init__(sender)
        self.message = message
