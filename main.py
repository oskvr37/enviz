from enviz import Env

env = Env('.env.example', True)

variables = {
    'TEST1': '1',
    'TEST2': '2'
}

env.update(variables)

env['TEST3'] = '3'
