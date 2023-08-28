from quantifiers.quantifier import Quantifier
from utils import quantifier_utils


class acc(Quantifier):
    def predict(self, test_scores, thr=0.5, *args, **kwargs):
        count = sum(1 for i in test_scores if i >= thr)
        cc_ouput = round(count / len(test_scores), 2)

        tprfpr = quantifier_utils.find_tprfpr_by_threshold(self.tprfpr, thr)

        tpr_fpr_difference = tprfpr["tpr"] - tprfpr["fpr"]
        pos_prop = (cc_ouput - tprfpr["fpr"]) / tpr_fpr_difference

        # Clamp pos_prop between 0 and 1
        pos_prop = max(0, min(1, pos_prop))

        return pos_prop
