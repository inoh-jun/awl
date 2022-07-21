import numpy as np
import pandas as pd


class PCA:
    def __init__(self, X):
        '''
        ## initialization
        X: trainig data (N*次元数, numpy.ndarray)
        '''

        # 中心化
        self.mean = np.mean(X, axis=0)
        self.X = X - self.mean

        def reduceDim(self, lowerDim):
            '''
            ## 次元削減
            lowerDim: 低次元空間の次元数(スカラー(整数))
            '''

            # 分散共分散行列
            cov = np.cov(self.X.T, bias=1)
