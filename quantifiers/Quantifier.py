from abc import ABC, abstractmethod


class Quantifier(ABC):
    @abstractmethod
    def setTprFpr(self, X_train):
        pass

    @abstractmethod
    def predict(self, X_test):
        pass
