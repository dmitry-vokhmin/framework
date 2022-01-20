from abc import ABCMeta, abstractmethod


class CommandsInvoker:
    def __init__(self):
        self._commands_list = []

    def store_command(self, command):
        self._commands_list.append(command)

    def execute_commands(self):
        for command in self._commands_list:
            command.execute()


class Command(metaclass=ABCMeta):
    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class ActionCommand(Command):
    def execute(self):
        self._receiver.action()


class PauseCommand(Command):
    def execute(self):
        self._receiver.pause()


class CommandsReceiver:
    def action(self):
        print('action in receiver')

    def pause(self):
        print('pause in receiver')


# пульт
commands_invoker = CommandsInvoker()

# внутренняя логика работа кнопок
commands_receiver = CommandsReceiver()

# кнопки
action_command = ActionCommand(commands_receiver)
pause_command = PauseCommand(commands_receiver)

# добавляем  кнопки на пульт
commands_invoker.store_command(action_command)
commands_invoker.store_command(pause_command)

commands_invoker.execute_commands()
