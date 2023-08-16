#!/usr/bin/python3

def multiple_returns(sentence):
    len_s = len(sentence)
    if len_s:
        return (len_s, sentence[0])
    return (0, None)
