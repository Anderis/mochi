import random

def get_response(message: str) -> str:
    message = message.lower()

    if message == 'hello':
        return 'Woof!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if message == '!help':
        return '`This is a help message you can modify`'

    if message == 'mochi':
        return 'woof?'

    if message == 'good girl':
        return 'WOOF WOOF!'
