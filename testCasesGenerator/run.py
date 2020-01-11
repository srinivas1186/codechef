import argparse
import json
from service.logicfile import generateTestCases

# Command line arguments setup
parser = argparse.ArgumentParser(description="Generates test cases according to the schema")
parser.add_argument('--schema', type=str, help="Name of the schema file")
parser.add_argument('--output', type=str, help="Name of the output file")
args = parser.parse_args()

schemaFileName = args.schema or "./schema.json"
outputFileName = args.output or "./output.txt"

# print("The schema file name is: " + schemaFileName)
# print("The output file name is: " + outputFileName)

with open(schemaFileName) as schemaFile:
    schema = json.load(schemaFile)

with open(outputFileName, "w") as outputFile:
    generateTestCases(schema, outputFile)
