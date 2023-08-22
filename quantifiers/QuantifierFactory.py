from quantifiers import Quantifier
from quantifiers.classify_count import ClassifyCount


class QuantifierFactory:
    def create_quantifier(self, quantifier_type):
        quantifier_type = quantifier_type.lower()
        if quantifier_type == "cc":
            return ClassifyCount()
