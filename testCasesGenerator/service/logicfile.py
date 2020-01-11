from service.parseObject import randomObject

def generateTestCases(schema, outputFile):
    # Storing reference array lengths
    arrayLengths = {}
    for placeholder in schema["structure"]:
        rule = schema[placeholder]
        if rule["type"] == "array":
            arrayLengths[rule["length"]] = -1
            
    # Parsing the placeholders
    for placeholder in schema["structure"]:
        rule = schema[placeholder]
        result = randomObject(rule, arrayLengths)
        if placeholder in arrayLengths.keys():
            arrayLengths[placeholder] = result
        print(result)

