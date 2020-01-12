from service.parseObject import randomObject

def generateTestCase(schema, outputFile):
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

def generateTestCases(schema, outputFile):
    numberOfTestCases = 1
    testCases = schema.get("testCases")
    if testCases != None:
        if "number" in testCases.keys():
            numberOfTestCases = testCases["number"]
        shouldPrintNumberOfTestCases = testCases.get("shouldPrint")
        if shouldPrintNumberOfTestCases:
            print(numberOfTestCases)
    for _ in range(numberOfTestCases):
        generateTestCase(schema, outputFile)