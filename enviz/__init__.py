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


env = {}

with open(".env", "r") as f:
    for line in f.readlines():
        key, value = read_line(line)
        if key is not None:
            env[key] = value

print(f"✅ [enviz] loaded .env | {len(env)} variables")
