from quantifiers.quantifier import Quantifier
from utils import quantifier_utils
import numpy as np


class pacc(Quantifier):
    def predict(self, X_test, thr=0.5, *args, **kwargs):
        # TODO: Calibrar
        calibrated_predictions = X_test
        tprfpr = quantifier_utils.find_tprfpr_by_threshold(self.tprfpr, thr)
        pos_prop = np.mean(calibrated_predictions)
        diff_tpr_fpr = tprfpr["tpr"] - tprfpr["fpr"]
        pos_prop = (pos_prop - tprfpr["fpr"]) / diff_tpr_fpr

        # Clamp pos_prop between 0 and 1
        pos_prop = max(0, min(1, pos_prop))

        return pos_prop
