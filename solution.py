import pandas as pd
import numpy as np
import scipy as sp

chat_id = 6064443932 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    stats, pvalue = ttest_ind(x, y, equal_var=False, alternative="greater")
    return stats > 0 and pvalue < 0.09
