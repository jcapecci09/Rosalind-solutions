"""Here we will be using probabilities to calculate percent chance of 
offspring contaning a dominant allele
author: Jimmy Capecci
"""
m = 20
n = 20
k = 20
total = m + n + k

event_mm = m/total * ((m-1) / (total-1)) * 0.25
event_nn = n/total * ((n-1) / (total-1)) * 1
event_mn = m/total * ((n) / (total-1)) * 0.5
event_nm = n/total * ((m) / (total-1)) * 0.5

probability = 1 - (event_mn + event_mm + event_nm + event_nn)

print(probability)