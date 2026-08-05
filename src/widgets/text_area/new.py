def view_update(data=None, location=None):
    print("\033[?7l" + "\033[2J\033[3J\033[H", end="")

    print(
        "\n".join(["".join(line) for line in data or []]),
        flush=True
    )

    if location:
        print(
            f"\033[{location["y"]+1};{location["x"]+1}H",
            end="",
            flush=True
        )
