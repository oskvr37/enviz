import logging
from .env import Env


GRAY, CYAN, GREEN, RESET = "\033[90m", "\033[96m", "\033[92m", "\033[0m"


logging.basicConfig(
    level=logging.DEBUG,
    format=f"{GRAY}%(asctime)s {GREEN}%(levelname)s{RESET} <%(name)s> :: %(message)s",
    datefmt="[ %Y-%m-%d %X ]",
)
