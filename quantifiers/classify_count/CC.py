from quantifiers.quantifier import Quantifier


class cc(Quantifier):
    def setTprFpr(self, X_train, y_train):
        pass

    def predict(self, X_test, thr=0.5, *args, **kwargs):
        count = len([i for i in X_test if i >= thr])
        pos_prop = round(count / len(X_test), 2)
        return pos_prop
