import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1897874711 # Ваш chat ID, не меняйте название переменной

def solution(control: np.ndarray, test: np.ndarray) -> bool:
    alpha = 0.09
    result = ttest_ind(control, test)
    return result.pvalue/2 < alpha and result.statistic > 0
