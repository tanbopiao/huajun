"""化钧（HUAJUN）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_evolve(self):
        ok = self.op.evolve("候选甲", 0.9)
        self.assertEqual(ok["status"], "enabled")
        sealed = self.op.evolve("候选乙", 0.5)
        self.assertEqual(sealed["status"], "sealed")

    def test_seal(self):
        out = self.op.seal("候选丙")
        self.assertTrue(out["sealed"])


if __name__ == "__main__":
    unittest.main()
