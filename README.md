<img src="https://raw.githubusercontent.com/oskvr37/enviz/main/logo.svg" width="100%"/>

# About

Enviz is a python module that allows you to write and read environment variables from a file.

# Installation

```bash
pip install enviz
```

# Usage

```python
from enviz import Env

# Read environment variables from a file
env = Env(path='.env.example', autowrite=True)

# We can update the environment variables with a dictionary
env.update({
    'TEST1': '1',
    'TEST2': '2'
})

# We can also update the environment variables by setting them manually
env['TEST3'] = '3'
```

```bash
# env.example
TEST1 = "1"
TEST2 = "2"
TEST3 = "3"
```

Enviz will automatically write the environment variables to the file if the `autowrite` parameter is set to `True`. If you want to write the environment variables manually, you can use the `write()` method.
