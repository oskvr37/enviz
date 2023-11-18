env = dict()

with open(".env", "r") as f:
    for line in f.readlines():
        if line.startswith("#"):
            continue
        
        key, value = '', ''
        for i, c in enumerate(line):
            if c == '=':
                key = line[:i]
                value = line[i+1:-1]
                break
        
        env[key] = value

print(f'✅ loaded .env | {len(env)} variables')
