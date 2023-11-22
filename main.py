from enviz import Env

env = Env(path='.env.example', autowrite=True)

env.update({
    'TEST1': '1',
    'TEST2': '2'
})

env['TEST3'] = '3'
