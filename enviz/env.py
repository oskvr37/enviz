import re

CYAN, GREEN, RESET = "\033[96m", "\033[92m", "\033[0m"


def read_line(line):
    pattern = re.compile(r'^\s*([\w.-]+)\s*=\s*([\'"])([^\'"]*?)\2\s*(?:#.*)?$')
    match = pattern.match(line)

    if match:
        key, value = match.group(1), match.group(3)
        print(f"{CYAN}{key}{RESET} = {GREEN}{value}{RESET}")
        return key, value
    else:
        return None, None


class Env(dict):
    """
    # Env Class
    - read .env file
    - format .env file
    - update variables
    - delete the variables
    """

    def __init__(self, __path: str = ".env") -> None:
        env = {}
        with open(__path, "r") as f:  # what if file not found?
            for line in f.readlines():
                key, value = read_line(line)
                if key is not None:
                    env[key] = value

        super().__init__(env)

    def __setitem__(self, __key: str, __value: str) -> None:
        super().__setitem__(__key, __value)
        self.write()
        return super().__getitem__(__key)

    def __getitem__(self, __key: str) -> str:
        return super().__getitem__(__key)

    def __delitem__(self, __key: str) -> None:
        super().__delitem__(__key)
        self.write()
        return None

    def write(self, path=".env.tmp"):
        def format_line(key, value, format='{} = "{}"', comment=""):
            if comment:
                return format.format(key, value) + f"\t# {comment}\n"
            return format.format(key, value) + "\n"

        with open(path, "w") as f:
            for key, value in self.items():
                f.write(format_line(key, value))
