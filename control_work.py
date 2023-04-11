# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:01:55 2023

@author: romas
"""

import math as m

import scipy.stats as scpst

print()


def main_work(arr_main: list, element: float):
    
    arr = [x for x in arr_main if x != element]

    y_mean, s_k, check = count_t(arr, element, q)

    if check:
        
        arr_main.remove(element)
        
def count_basic_features(arr: list):
    
    df = len(arr)-1

    y_mean = sum(arr)/len(arr)

    print(f"y_mean = {y_mean}")

    S_k = sum(list(map(lambda x: (x-y_mean)**2, arr)))/df

    print(f"S_k = {S_k}")

    s_k = m.sqrt(S_k)

    print(f"s_k = {s_k}")
    
    return y_mean, s_k
    

def count_t(arr: list, element: int, q: float):
    
    print(f"Перевіряємо елемент {element}")
    
    df = len(arr)-1

    y_mean, s_k = count_basic_features(arr)
    
    t = abs(element - y_mean) / s_k
    
    t_stat = scpst.t.ppf(q=1-q, df=df)
    
    if t > t_stat:
        
        print(f"Значення критерію Стьюдента: {t} > {t_stat}")
        
        print(f"{element} є грубою помилкою")
        
        print()
        
        return y_mean, s_k, True
    
    else:
        
        print(f"Значення критерію Стьюдента: {t} < {t_stat}")
        
        print(f"{element} не є грубою помилкою")
        
        print()
        
        return y_mean, s_k, False
  

def count_delta(arr: list, q: float):
    
    y_mean, s_k = count_basic_features(arr)
    
    s_y = s_k/(m.sqrt(len(arr)))
    
    print(f"s_y = {s_y}")
    
    df = len(arr)-1
    
    t_stat = scpst.t.ppf(q=1-q, df=df)
    
    eps_y = t_stat*s_y
    
    print(f"ε_y = {eps_y}")
    
    delta = eps_y/y_mean
    
    print(f"Δ = {delta*100}%")
    
    
# array given in the variant
arr_main = [19.8, 21.01, 21.05, 21.06, 21.08, 22.01, 27.3]

# level of significance
q = 0.05

main_work(arr_main, arr_main[0])

main_work(arr_main, arr_main[-1])

count_delta(arr_main, q)