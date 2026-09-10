def greet(name: str) -> str:
    if name == "":
        raise ValueError("name must not be empty")
    return f"안녕, {name}!"
