#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for BuyInsurance

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_BuyInsurance = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_BuyInsurance.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_BuyInsurance:
        print("[BuyInsurance] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]想保[旅(行)險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {} 。你要買多少天的 {} ？".format(args[1], args[1])
            

    if utterance == "[我]想幫家人買[一份][醫療保單]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {} 。 {} 是針對幾歲的人？ 性別是男是女？".format(args[2], args[2])
            

    if utterance == "[我]想要了解一下關於[醫療]的[保險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {} {} 。 {} 是針對幾歲的人？ 性別是男是女？".format(args[1], args[2], args[2])
            

    if utterance == "[我]想要了解關於[終生型]的[醫療][保險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {} 。 {}  {} 是針對幾歲的人？ 性別是男是女？".format(args[1], args[2], args[3])
            

    if utterance == "[我]想要幫[家人]買[一份][保險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {} 。 {} 是幾歲？ 性別是男是女？".format(args[3], args[1])
            

    if utterance == "[我]想要幫[自己]投保":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種。你想要住院醫療相關還是壽險？"
            

    if utterance == "[我]想要幫[自己]買[保險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {}。你想要住院醫療相關還是壽險？".format(args[2])
            

    if utterance == "[我]想買[保險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {}。你想要住院醫療相關還是壽險？".format(args[1])
            

    if utterance == "出國時保哪一種[保險]比較適合":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {} 。你要買多少天的 {} ？".format(args[0], args[0])
            

    if utterance == "詢問出國的旅行[保險]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {} 。你要買多少天的 {} ？".format(args[0], args[0])
            

    if utterance == "針對[老人家]，什麼[保單]比較適合":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "我們有很多種 {} 。 {} 的年紀多大？ 性別是男還是女？".format(args[1], args[0])
            

    return resultDICT