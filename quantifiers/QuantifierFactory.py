from quantifiers import Quantifier
from quantifiers.classify_count.ClassifyCount import ClassifyCount


class QuantifierFactory:
    def create_quantifier(self, quantifier_type):
        quantifier_type = quantifier_type.lower()
        if quantifier_type == 'cc':
            return ClassifyCount()
        elif quantifier_type == 'acc':
            return None
        elif quantifier_type == 'pcc':
            return None
        elif quantifier_type == 'pacc':
            return None
        elif quantifier_type == 'x':
            return None
        elif quantifier_type == 'max':
            return None
        elif quantifier_type == 't50':
            return None
        elif quantifier_type == 'ms':
            return None
        elif quantifier_type == 'hdy':
            return None
        elif quantifier_type == 'dys':
            return None
        elif quantifier_type == 'sord':
            return None
        else:
            print(f'Invalid quantifier: {quantifier_type}')
            return None
