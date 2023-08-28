import pandas as pd
import numpy as np

from quantifiers.quantifier import Quantifier
from utils import quantifier_utils


class dys(Quantifier):
    def predict(self, test_scores, *args, **kwargs):
        bin_size = np.linspace(10, 110, 11)
        result = []
        for bins in bin_size:
            p_bin_count = quantifier_utils.get_hist(self.pos_scores, bins)
            n_bin_count = quantifier_utils.get_hist(self.neg_scores, bins)
            te_bin_count = quantifier_utils.get_hist(test_scores, bins)

            def f(x):
                return quantifier_utils.DyS_distance(
                    ((p_bin_count * x) + (n_bin_count * (1 - x))),
                    te_bin_count,
                    measure="topsoe",
                )

            result.append(quantifier_utils.ternary_search(0, 1, f))
        pos_prop = np.median(result)
        return pos_prop

