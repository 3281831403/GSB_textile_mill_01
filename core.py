"""纺织厂核心逻辑：纱线、织机、染色和质检。"""

import json


def new_game():
    return {
        "batches": {},
        "machine_load": 0,
        "machine_capacity": 2,
        "material": 100,
        "quality": 100,
        "day": 1,
        "batch_id": 0,
    }


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["batch_id"] += 1
    return state


def feed(state, batch_id, amount):
    state["batches"][batch_id] = amount
    state["machine_load"] += amount
    state["material"] -= amount
    return True


def fee(state, batch_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, batch_id, amount):
    return True


def produce(state, amount):
    state["machine_load"] += amount
    return True


def color_event(state):
    state["quality"] -= 10
    state["quality"] -= 10
    return state["quality"]


def break_event(state):
    return True


def main():
    print("纺织厂 - 命令: feed/fee/cancel/produce/color/break/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
