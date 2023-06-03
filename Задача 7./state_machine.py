import re

KEYS = {
    '-a': {'param': True},
    '-r': {'param': True},
    '-p': {'param': True},
    '-n': {'param': False},
    '-m': {'param': False},
    '-l': {'param': False},
    '-s': {'param': False},
    '-c': {'param': False},
}


def parse_command_line(command_line):
    words = re.findall(r'("-.*?"|\S+)', command_line)
    state, command, params, keys, current_key = 'command', None, [], {}, None

    for word in words:
        word = word.strip('"').replace('_', ' ')

        if state == 'command':
            if re.match(r'^[a-zA-Z]+$', word):
                command = word
                state = 'params'
            else:
                raise Exception('Invalid command format')
        elif state == 'params':
            if word in KEYS:
                state = 'keys'
                current_key = word
                keys[current_key] = []
            elif re.match(r'^[\w\s]+$', word):
                params.append(word)
            else:
                raise Exception('Invalid parameter format')
        elif state == 'keys':
            if word in KEYS:
                if KEYS[current_key]['param'] and len(keys[current_key]) == 0:
                    raise Exception(f'Key {current_key} requires a parameter')
                current_key = word
                keys[current_key] = []
            elif re.match(r'^[\w\s]+$', word):
                if KEYS[current_key]['param'] or len(keys[current_key]) == 0:
                    keys[current_key].append(word)
                else:
                    raise Exception(f'Key {current_key} does not allow parameters')
            else:
                raise Exception('Invalid key parameter format')

    if current_key and KEYS[current_key]['param'] and len(keys[current_key]) == 0:
        raise Exception(f'Key {current_key} requires a parameter')

    return command, params, keys


if __name__ == '__main__':
    command_line = input('Enter a command line: ')
    command, params, keys = parse_command_line(command_line)
    print(f'Command: {command}\nParams: {params}\nKeys: {keys}')

    inp_str1 = 'command param1 param2 -a keyParam1 -r keyParam2 -c'
    inp_str2 = 'command param1 -a "multi word param"'
    inp_str3 = 'command param1 param2'

