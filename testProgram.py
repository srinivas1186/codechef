import os
import subprocess
import time
import sys

pwd = os.getcwd()

args = sys.argv[1:]

programTestTypes = ("-p",'-c','-cp','-j')
print(args)
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
def runProgram(command:list,testFile:str):
    # command = ['python3','/home/sri/Desktop/c1.py']
    with open(testFile) as testCase:
        t1 = time.time()
        temp = subprocess.run(command,stdin=testCase,capture_output=True)
        time_taken = time.time() - t1
        # print(str(temp.stdout))
        out_data = temp.stdout
        if temp.returncode == 0:
            print("Output: ")
            print(out_data.decode('utf-8'))
        else:
            print('Error occured')
            print(temp.stderr)
        print('Completed in {}\n'.format(time_taken))



def timeIt(func):

    def wrapper():
        t1 = time.time()
        func()
        print("Complete in {0}".format(time.time()-t1))
    
    return wrapper

@timeIt
def testC():
    prog = os.path.join(program_dir,'language',programTypeFolderMap[args[0]],programToTest+'.c')
    if not os.path.exists(prog):
        print(prog,"--> Doesnt exist create the file")
        exit(1)
        return
    prog_after = os.path.join(program_dir,'language',programTypeFolderMap[args[0]],programToTest)
    print('Compiling the c code')
    temp = subprocess.Popen(['gcc',prog,'-o',prog_after], stdout=subprocess.PIPE)
    temp.communicate()
    print('Compilation complete\n')
    testCaseFol = os.path.join(program_dir,"testCases")
    for root,dirs,files in os.walk(testCaseFol):
        for testcase in files:
            print('--\nTest case file: {}'.format(testcase))
            runProgram([prog_after],os.path.join(root,testcase))
            print('--')
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
    testCaseFol = os.path.join(program_dir,"testCases")
    # print('Running {}\n\n'.format(prog))
    for root,dirs,files in os.walk(testCaseFol):
        for testcase in files:
            print('--\nTest case file: {}'.format(testcase))
            runProgram(['python3',prog],os.path.join(root,testcase))
            print('--')
            
    # print(prog)
    # pass


def test():
    pass

if __name__=="__main__":
    # print("working")
    print('Running {}'.format(programToTest))
    if args[0] == '-c':
        testC()
    elif args[0] == '-cp':
        testCpp()
    elif args[0] == '-p':
        testPython()
    elif args[0] == '-j':
        testJava()
    else:
        print('Type not found')