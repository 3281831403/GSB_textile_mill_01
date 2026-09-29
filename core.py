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
    return json.loads(text)


def feed(state, batch_id, amount):
    if state.get("stopped"):
        return False
    if batch_id in state["batches"]:
        return False
    if state["machine_load"] + 1 > state["machine_capacity"]:
        return False
    state["batches"][batch_id] = amount
    state["machine_load"] += 1
    state["material"] -= amount
    return True


def fee(state, batch_id, end_day):
    return end_day - state["day"]


def cancel(state, batch_id, amount):
    fed = state["batches"].get(batch_id)
    if fed is None or amount <= 0 or amount > fed:
        return False
    state["material"] += amount
    remaining = fed - amount
    if remaining:
        state["batches"][batch_id] = remaining
    else:
        del state["batches"][batch_id]
        state["machine_load"] -= 1
    return True


def produce(state, amount):
    if state.get("color_fault") or state.get("stopped"):
        return False
    state["machine_load"] += amount
    return True


def color_event(state):
    state["quality"] -= 10
    return state["quality"]


def break_event(state):
    state["stopped"] = True
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
