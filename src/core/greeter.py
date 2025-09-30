def greeting(name: str = "") -> str:
    name = name or "world"
    return f"Hello, {name}!"
