"""化钧（HUAJUN）· 受控演化，衡分达标方可启用

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：受控演化，衡分达标方可启用。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Huajun:
    """化钧（HUAJUN）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "HUAJUN"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.records = []
        self.sealed = set()

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "huajun",
            "cn": "化钧",
            "code": self.CODE,
            "duty": "受控演化，衡分达标方可启用",
            "mingwen": "钧陶万变，衡准乃化",
            "anchor": self.ANCHOR,
        }

    def evolve(self, candidate, hengfen):
        """衡分达标方可放行演化，未达标封化待育。"""
        threshold = float(self.config.get("threshold", 0.8))
        passed = hengfen >= threshold
        record = {"candidate": candidate, "hengfen": hengfen,
                  "status": "enabled" if passed else "sealed"}
        self.records.append(record)
        self.events.append({"event": "evolve", "status": record["status"]})
        return record

    def seal(self, candidate):
        """封化：锁演化留档，非时不启。"""
        self.sealed.add(str(candidate))
        self.events.append({"event": "seal"})
        return {"candidate": candidate, "sealed": True}
