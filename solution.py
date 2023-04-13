import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1897874711 # Ваш chat ID, не меняйте название переменной

def solution(control: np.ndarray, test: np.ndarray) -> bool:
    alpha = 0.09 # уровень значимости критерия
    stat, p_value = ttest_ind(control, test, equal_var=False) # двухвыборочный t-критерий Стьюдента
    if p_value < alpha:
        return True # отклоняем нулевую гипотезу
    else:
        return False # не отклоняем нулевую гипотезу
