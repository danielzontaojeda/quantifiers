from quantifiers.quantifier import Quantifier


class PCC(Quantifier):
	def setTprFpr(self, X_train, y_train):
		pass

	def predict(self, X_test, thr=0.5):
		#TODO: Calibrar
		calibrated_predictions = X_test
		pcc_count = sum(calibrated_predictions[calibrated_predictions > thr])
		pos_prop = round(pcc_count/len(calibrated_predictions),2)
		
		# Clamp pos_prop between 0 and 1
		pos_prop = max(0, min(1, pos_prop))
		
		return pos_prop
