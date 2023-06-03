import re

class State:
    def handle(self, context, char):
        raise NotImplementedError

class CommandState(State):
    def handle(self, context, char):
        if re.match(r'[a-zA-Z]', char):
            context.command += char
            return self
        elif char.isspace():
            return SpaceState()
        else:
            raise ValueError('Неверный символ для состояния команды')

class SpaceState(State):
    def handle(self, context, char):
        if char.isspace():
            return self
        elif re.match(r'[a-zA-Z0-9]', char):
            context.parameters.append(char)
            return ParameterState()
        elif char == '-':
            return KeyState()
        else:
            raise ValueError('Неверный символ для состояния пробела')

class ParameterState(State):
    def handle(self, context, char):
        if char.isspace():
            return SpaceState()
        elif re.match(r'[a-zA-Z0-9]', char):
            context.parameters[-1] += char
            return self
        elif char == '-':
            return KeyState()
        else:
            raise ValueError('Неверный символ для состояния параметра')

class KeyState(State):
    def handle(self, context, char):
        if re.match(r'[a-z]', char):
            if char in context.keys:
                raise ValueError(f'Ключ -{char} уже использован')
            if char == 'a' or char == 'r' or char == 'p':
                context.keys.append(char)
                return KeyParameterState()
            elif char == 'n' or char == 'm' or char == 'l' or char == 's':
                context.keys.append(char)
                return OptionalKeyParameterState()
            elif char == 'c':
                context.keys.append(char)
                return self
            else:
                raise ValueError('Неизвестный ключ')
        elif char.isspace():
            return self
        else:
            raise ValueError('Неверный символ для состояния ключа')

class KeyParameterState(State):
    def handle(self, context, char):
        if re.match(r'[a-zA-Z0-9]', char):
            context.parameters.append(char)
            return ParameterState()
        elif char == '"':
            context.parameters.append('')
            return QuoteState()
        elif char.isspace():
            print(f"Warning: ключ -{context.keys[-1]} требует параметр.")
            return SpaceState()
        else:
            raise ValueError('Неверный символ для состояния параметра ключа. Параметр обязателен.')

class OptionalKeyParameterState(State):
    def handle(self, context, char):
        if char.isspace():
            print(f"Warning: ключ -{context.keys[-1]} может требовать параметр.")
            return SpaceState()
        elif re.match(r'[a-zA-Z0-9]', char):
            context.parameters.append(char)
            return ParameterState()
        elif char == '"':
            context.parameters.append('')
            return QuoteState()
        else:
            raise ValueError('Неверный символ для состояния параметра ключа')

class QuoteState(State):
    def handle(self, context, char):
        if char == '"':
            return SpaceState()
        else:
            context.parameters[-1] += char
            return self

class Context:
    def __init__(self):
        self.state = CommandState()
        self.command = ''
        self.parameters = []
        self.keys = []

    def process(self, char):
        self.state = self.state.handle(self, char)

    def process_string(self, string):
        for char in string:
            self.process(char)
        print(f'Command: {self.command}\nParameters: {self.parameters}\nKeys: {self.keys}')
        self.command = ''
        self.parameters.clear()
        self.keys.clear()

context = Context()
context.process_string('command -n parameter1 -a parameter2 -m parameter3')
#context.process_string('command -l -p parameter2 -s parameter3')
