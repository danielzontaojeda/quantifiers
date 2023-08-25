from quantifiers.classify_count import x, acc, cc, pacc, pcc, max, t50, ms
from abc import ABC


class QuantifierFactory(ABC):
    def create_quantifier(self, quantifier_type):
        quantifier_type = quantifier_type.lower()
        if quantifier_type == "cc":
            return cc.cc()
        elif quantifier_type == "acc":
            return acc.acc()
        elif quantifier_type == "pcc":
            return pcc.pcc()
        elif quantifier_type == "pacc":
            return pacc.pacc()
        elif quantifier_type == "x":
            return x.x()
        elif quantifier_type == "max":
            return max.MAX()
        elif quantifier_type == "t50":
            return t50.t50()
        elif quantifier_type == "ms":
            return ms.ms()
        elif quantifier_type == "hdy":
            return None
        elif quantifier_type == "dys":
            return None
        elif quantifier_type == "sord":
            return None
        else:
            print(f"Invalid quantifier: {quantifier_type}")
            return None
