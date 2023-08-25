from quantifiers.quantifier import Quantifier
import numpy as np


class PCC(Quantifier):
    def predict(self, X_test, *args):
        # TODO: Calibrar
        calibrated_predictions = X_test
        pos_prop = np.mean(calibrated_predictions)

        return pos_prop
