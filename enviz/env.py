import logging
import re


GRAY, CYAN, GREEN, RESET = "\033[90m", "\033[96m", "\033[92m", "\033[0m"

logger = logging.getLogger(__name__)


def read_file(path):
    def read_line(line):
        pattern = re.compile(r'^\s*([\w.-]+)\s*=\s*([\'"])([^\'"]*?)\2\s*(?:#.*)?$')
        match = pattern.match(line)

        if match:
            key, value = match.group(1), match.group(3)
            return key, value
        else:
            return None, None

    env = {}
    with open(path, "r") as f:
        for line in f.readlines():
            key, value = read_line(line)
            if key is not None:
                env[key] = value
    return env


class Env(dict):
    """
    Extends `dict`
    - read .env file
    - format .env file
    - update variables
    - delete the variables
    """

    def __init__(self, path=".env", autowrite=False) -> None:
        self.path = path
        self.autowrite = autowrite
        super().__init__({})
        self.read()

    def read(self):
        try:
            env = read_file(self.path)
            logger.info(
                f"🔧 Loaded {CYAN}{self.path}{RESET} with {GREEN}{len(env)}{RESET} variables"
            )
        except FileNotFoundError:
            env = {}
            logger.warning(
                f"🔧 {CYAN}{self.path}{RESET} not found, using {GREEN}empty{RESET} environment"
            )

        self.update(env)

    def __setitem__(self, __key: str, __value: str) -> None:
        super().__setitem__(__key, __value)
        self.auto_write()
        return super().__getitem__(__key)

    def __getitem__(self, __key: str) -> str:
        return super().__getitem__(__key)

    def update(self, __variables: dict) -> None:
        super().update(__variables)
        self.auto_write()
        return None

    def __delitem__(self, __key: str) -> None:
        super().__delitem__(__key)
        self.auto_write()
        return None

    def write(self, path=""):
        """
        Write the variables to provided `path`,
        if `path` is not provided, it will write to `self.path.tmp`
        """
        
        if self == {}:
            logger.warning(
                f"🔧 {CYAN}{self.path}{RESET} is empty, skipping write"
            )
            return

        logger.debug(
            f"⚡ Saving {CYAN}{path}{RESET} with {GREEN}{len(self)}{RESET} variables"
        )

        def format_line(key, value, format='{} = "{}"', comment=""):
            if comment:
                return format.format(key, value) + f"\t# {comment}\n"
            return format.format(key, value) + "\n"

        if path == "":
            path = f"{self.path}.tmp"

        with open(path, "w") as f:
            for key, value in self.items():
                f.write(format_line(key, value))

        logger.debug(
            f"✅ Saved {CYAN}{path}{RESET} with {GREEN}{len(self)}{RESET} variables"
        )

    def auto_write(self):
        if self.autowrite:
            self.write()
