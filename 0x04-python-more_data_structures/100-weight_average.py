#!/usr/bin/python3

def weight_average(my_list=[]):
    res = 0
    if my_list and len(my_list):
        scores, weights = (0, 0)
        for score, weight in my_list:
            scores += score * weight
            weights += weight
        res =  scores/weights
    return res
