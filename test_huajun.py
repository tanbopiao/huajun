"""化钧（HUAJUN）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from huajun import Huajun


class TestHuajun(unittest.TestCase):
    def setUp(self):
        self.op = Huajun()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "huajun")
        self.assertEqual(d["code"], "HUAJUN")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_evolve_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.evolve(None, None)

    def test_seal_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.seal(None)


if __name__ == "__main__":
    unittest.main()
