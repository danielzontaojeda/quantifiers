import pandas as pd

from quantifiers.quantifier import Quantifier
from utils import quantifier_utils


class ACC(Quantifier):
    def predict(self, test_scores, thr=0.5):
        count = sum(1 for i in test_scores if i >= thr)
        cc_ouput = round(count / len(test_scores), 2)

        tprfpr = self.tprfpr.query(f"threshold == {thr}")
        tprfpr.loc[:, "fpr"] = tprfpr["fpr"].astype(float)
        tprfpr.loc[:, "tpr"] = tprfpr["tpr"].astype(float)

        tpr_fpr_difference = tprfpr["tpr"].iloc[0] - tprfpr["fpr"].iloc[0]
        pos_prop = (cc_ouput - tprfpr["fpr"].iloc[0]) / tpr_fpr_difference

        # Clamp pos_prop between 0 and 1
        pos_prop = max(0, min(1, pos_prop))

        return pos_prop
