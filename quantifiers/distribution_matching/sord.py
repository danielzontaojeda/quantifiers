import pandas as pd
import numpy as np

from quantifiers.quantifier import Quantifier
from utils import quantifier_utils


class sord(Quantifier):
    def predict(self, test_scores, *args, **kwargs):
        alpha = np.linspace(0, 1, 101)
        sc_1 = self.pos_scores
        sc_2 = self.neg_scores
        ts = test_scores

        vDist = []
        for k in alpha:
            pos = np.array(sc_1)
            neg = np.array(sc_2)
            test = np.array(ts)
            pos_prop = k

            p_w = pos_prop / len(pos)
            n_w = (1 - pos_prop) / len(neg)
            t_w = -1 / len(test)

            p = list(map(lambda x: (x, p_w), pos))
            n = list(map(lambda x: (x, n_w), neg))
            t = list(map(lambda x: (x, t_w), test))
            print(p)

            v = sorted(p + n + t, key=lambda x: x[0])

            acc = v[0][1]
            total_cost = 0

            for i in range(1, len(v)):
                cost_mul = v[i][0] - v[i - 1][0]
                total_cost = total_cost + abs(cost_mul * acc)
                acc = acc + v[i][1]

            vDist.append(total_cost)

        pos_prop = alpha[vDist.index(min(vDist))]
        return pos_prop
