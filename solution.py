import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 6064443932 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    return ztest(x, y, alternative='larger')[1] < 0.09
