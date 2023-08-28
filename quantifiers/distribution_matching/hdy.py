import pandas as pd
import numpy as np

from quantifiers.quantifier import Quantifier
from utils import quantifier_utils


class hdy(Quantifier):
    def predict(self, test_scores, *args, **kwargs):
        bin_size = np.linspace(10, 110, 11)
        alpha_values = np.linspace(0, 1, 101)
        return None

    def set_scores(self, train_test_scores):
        scores = {
            "scores": train_test_scores["X_train"],
            "class": train_test_scores["y_train"],
        }
        df = pd.DataFrame(scores)
        self.pos_scores = df.query("`class`== 1")
        self.neg_scores = df.query("`class` == 0")
