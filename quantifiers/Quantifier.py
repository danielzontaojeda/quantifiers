from abc import ABC, abstractmethod


class Quantifier(ABC):
    @abstractmethod
    def setTprFpr(self, X_train, y_train):
        pass

    @abstractmethod
    def predict(self, X_test):
        pass
