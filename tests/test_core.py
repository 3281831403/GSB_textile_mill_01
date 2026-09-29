import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_feed(self):
        state = core.new_game()
        self.assertTrue(core.feed(state, 1, 10))
        self.assertFalse(core.feed(state, 1, 10))

    def test_02_machine_capacity(self):
        state = core.new_game()
        state["machine_load"] = 2
        result = core.feed(state, 2, 1)
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, 1, 3), 2)

    def test_04_cancel_refunds(self):
        state = core.new_game()
        core.feed(state, 1, 5)
        core.cancel(state, 1, 5)
        self.assertEqual(state["material"], 100)

    def test_05_no_produce_on_fault(self):
        state = core.new_game()
        state["color_fault"] = True
        result = core.produce(state, 5)
        self.assertFalse(result)

    def test_06_color_event_once(self):
        state = core.new_game()
        core.color_event(state)
        self.assertEqual(state["quality"], 90)

    def test_07_break_stops_machine(self):
        state = core.new_game()
        core.break_event(state)
        self.assertTrue(state.get("stopped"))

    def test_08_load_preserves_batch(self):
        state = core.new_game()
        state["batch_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["batch_id"], 4)


if __name__ == "__main__":
    unittest.main()
