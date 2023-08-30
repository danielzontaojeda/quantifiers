import pandas as pd
import numpy as np

from utils.distances import Distances


def getTPRandFPRbyThreshold(validation_scores):
    unique_scores = np.arange(0, 1, 0.01)
    arrayOfTPRandFPRByTr = pd.DataFrame(columns=['threshold', 'fpr', 'tpr'])
    total_positive = len(validation_scores[validation_scores['class'] == 1])
    total_negative = len(validation_scores[validation_scores['class'] == 0])

    aux = pd.DataFrame(columns=['threshold', 'fpr', 'tpr'])

    for threshold in unique_scores:
        fp = len(
            validation_scores[
                (validation_scores['score'] > threshold)
                & (validation_scores['class'] == 0)
            ]
        )
        tp = len(
            validation_scores[
                (validation_scores['score'] > threshold)
                & (validation_scores['class'] == 1)
            ]
        )
        tpr = round(tp / total_positive, 2)
        fpr = round(fp / total_negative, 2)

        aux.loc[threshold] = [round(threshold, 2), fpr, tpr]

    arrayOfTPRandFPRByTr = pd.concat([arrayOfTPRandFPRByTr, aux])
    arrayOfTPRandFPRByTr.reset_index(inplace=True, drop=True)

    return arrayOfTPRandFPRByTr


def find_tprfpr_by_threshold(tprfpr, threshold):
    tprfpr_threshold = {}
    instance = tprfpr.query(f'threshold == {threshold}')
    tprfpr_threshold['fpr'] = instance['fpr'].iloc[0].astype(float)
    tprfpr_threshold['tpr'] = instance['tpr'].iloc[0].astype(float)
    return tprfpr_threshold


def get_hist(scores, nbins):
    breaks = np.linspace(0, 1, int(nbins) + 1)
    breaks = np.delete(breaks, -1)
    breaks = np.append(breaks, 1.1)

    re = np.repeat(1 / (len(breaks) - 1), (len(breaks) - 1))
    for i in range(1, len(breaks)):
        re[i - 1] = (
            re[i - 1]
            + len(np.where((scores >= breaks[i - 1]) & (scores < breaks[i]))[0])
        ) / (len(scores) + 1)

    return re


def DyS_distance(sc_1, sc_2, measure):
    '''This function applies a selected distance metric'''

    dist = Distances(sc_1, sc_2)

    if measure == 'topsoe':
        return dist.topsoe()
    if measure == 'probsymm':
        return dist.probsymm()
    if measure == 'hellinger':
        return dist.hellinger()
    return 100


def ternary_search(left, right, f, eps=1e-4):
    '''This function applies Ternary search'''

    while True:
        if abs(left - right) < eps:
            return (left + right) / 2

        leftThird = left + (right - left) / 3
        rightThird = right - (right - left) / 3

        if f(leftThird) > f(rightThird):
            left = leftThird
        else:
            right = rightThird
