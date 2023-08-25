from abc import ABC, abstractmethod
from utils import quantifier_utils
import pandas as pd


class Quantifier(ABC):
    def setTprFpr(self, X_train, y_train):
        validation_scores = pd.DataFrame(columns=["class", "score"])
        validation_scores["class"] = y_train
        validation_scores["score"] = X_train
        self.tprfpr = quantifier_utils.getTPRandFPRbyThreshold(validation_scores)

    @abstractmethod
    def predict(self, X_test):
        pass
