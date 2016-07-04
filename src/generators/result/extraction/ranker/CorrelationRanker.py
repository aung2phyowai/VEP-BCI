import sklearn.cross_decomposition
import sklearn.preprocessing
import numpy as np

import Ranker


class CorrelationRanker(Ranker.RankerWithReferenceSignals):
    def __init__(self):
        Ranker.RankerWithReferenceSignals.__init__(self)

    def getCorr(self, signal, reference):
        raise NotImplementedError("getCorr not implemented!")

    def changeReferenceSignalLength(self, target_reference, length, is_short):
        if is_short:
            return np.array([target_reference[j][:length] for j in range(len(target_reference))])
        else:
            return np.array(target_reference)

    def getResults(self, coordinates, length, target_freqs, is_short):
        return self.getRanking(
            (freq, self.getCorr(coordinates, self.changeReferenceSignalLength(reference, length, is_short).T))
            for freq, reference in zip(target_freqs, self.reference_signals)
        )


class LrtRanker(CorrelationRanker):
    def __init__(self):
        CorrelationRanker.__init__(self)

    def setup(self, options):
        """
        Centralise reference signals (along samples).
        :param options: Dictionary of options
        :return:
        """
        CorrelationRanker.setup(self, options)
        for i in range(len(self.reference_signals)):
            sklearn.preprocessing.scale(self.reference_signals[i], axis=1, with_std=False)

    def getCorr(self, signal, reference):
        """
        Replace canonical correlation calculation with LRT.
        Centralises signal.
        :param signal: Multidimensional input signal. Shape: (window length, number of sensors).
        :param reference: Centralised reference signals for one target. Shape: (window length, 2 times the number
        of harmonics)
        :return: LRT result
        """
        sklearn.preprocessing.scale(signal, axis=1, with_std=False)  # centralise samples
        X = np.column_stack((signal, reference))
        sigma_hat = np.cov(X, rowvar=False)
        sigma_11 = np.cov(signal, rowvar=False)
        sigma_22 = np.cov(reference, rowvar=False)
        V = np.linalg.det(sigma_hat)/(np.linalg.det(sigma_11)*np.linalg.det(sigma_22))
        p2 = reference.shape[1]
        C = 1-V**(1.0/p2)
        return C


class CcaRanker(CorrelationRanker):
    def __init__(self):
        CorrelationRanker.__init__(self)
        self.model = None

    def setup(self, options):
        CorrelationRanker.setup(self, options)
        self.model = sklearn.cross_decomposition.CCA(n_components=1)

    def getCorr(self, signal, reference):
        self.model.fit(signal, reference)
        res_x, res_y = self.model.transform(signal, reference)
        corr = np.corrcoef(res_x.T, res_y.T)[0][1]
        return corr
