from quantifiers.classify_count import CC, ACC, PCC, PACC, X
from abc import ABC


class QuantifierFactory(ABC):
    def create_quantifier(self, quantifier_type):
        quantifier_type = quantifier_type.lower()
        if quantifier_type == "cc":
            return CC.CC()
        elif quantifier_type == "acc":
            return ACC.ACC()
        elif quantifier_type == "pcc":
            return PCC.PCC()
        elif quantifier_type == "pacc":
            return PACC.PACC()
        elif quantifier_type == "x":
            return X.X()
        elif quantifier_type == "max":
            return None
        elif quantifier_type == "t50":
            return None
        elif quantifier_type == "ms":
            return None
        elif quantifier_type == "hdy":
            return None
        elif quantifier_type == "dys":
            return None
        elif quantifier_type == "sord":
            return None
        else:
            print(f"Invalid quantifier: {quantifier_type}")
            return None
