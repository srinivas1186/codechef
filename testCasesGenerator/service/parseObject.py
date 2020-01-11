import random
import string

randomNumberDict = {
    "integer": random.randint,
    "float": random.uniform
}

def randomNumber(rule):
    lt = rule["range"].get("lt")
    gt = rule["range"].get("gt")
    return randomNumberDict[rule["type"]](gt, lt)

def randomString(rule): 
    maxSize = 100
    if rule.get("maxSize") != None:
        maxSize = rule.get("maxSize")
    alphabets = string.ascii_letters
    return "".join(random.choice(alphabets) for _ in range(random.randint(1, maxSize)))

def randomArray(rule, arrayLengths):
    elementType = rule["elementType"]
    seperator = "\n"
    if rule.get("seperator") != None:
        seperator = rule["seperator"]
    length = rule["length"]
    if type(rule["length"]) == str:
        length = arrayLengths[rule["length"]]
    return seperator.join(str(randomObject(elementType, arrayLengths)) for _ in range(length))

def randomObject(rule, arrayLengths):
    if rule["type"] in randomNumberDict.keys():
        return randomNumber(rule)
    elif rule["type"] == "string":
        return randomString(rule)
    elif rule["type"] == "array":
        return randomArray(rule, arrayLengths)