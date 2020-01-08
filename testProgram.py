import os
import subprocess
import time
import sys

pwd = os.getcwd()

args = sys.argv[1:]

programTestTypes = ("-p",'-c','-cp','-j')

programTypeMap = {'-p':".py",'-c':'.c','-cp':'.cpp','-j':'.java'}
programTypeFolderMap = {'-p':"python",'-c':'C','-cp':'c++','-j':'java'}

if len(args) < 2:
    print("Need to pass program type and program name as argument to run the test cases")
    print("Allowed types")
    print(*programTestTypes)
    print("example \"python3 testProgram.py -py 'somename'\"")
    exit(1)


programType = args[0] if args[0] in programTestTypes else '-py'

programToTest = args[1]  # In future this can be array of program names rather than just one program name

testCaseFile = []

def findProgram(name):

    for root,dirs,files in os.walk(pwd):
        for dir in dirs:
            if name == dir:
                return os.path.join(root,dir)
    return ""

program_dir = findProgram(programToTest)

if not program_dir:
    print("{} is not present".format(programToTest))
    exit(1)

# if program_dir:
#     print(program_dir)
#     exit(0)

def timeIt(func):

    def wrapper():
        t1 = time.time()
        func()
        print("Complete in {0}".format(time.time()-t1))
    
    return wrapper

@timeIt
def testC():
    pass

@timeIt
def testCpp():
    pass

@timeIt
def testJava():
    pass

@timeIt
def testPython():
    prog = os.path.join(program_dir,'language',programTypeFolderMap[args[0]],programToTest+".py")
    print(prog)
    pass


def test():
    pass

if __name__=="__main__":
    print("working")
    testPython()