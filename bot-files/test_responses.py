import random

def get_response(message: str) -> str:
    message = message.lower()

    if message == 'hello':
        greeting = '**WOOF!**\n*`... Mochi appears to be greeting you ...`*\n'
        return greeting

    if message == 'mochi':
        return 'woof?'

    if message == 'good girl':
        return 'WOOF WOOF!'

    if message == 'sit':
        return '**`Mochi sits begrudgingly, awaiting a treat.`**'
