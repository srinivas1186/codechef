#!/usr/bin/python3
import os
import sys

pwd = os.getcwd()
args = sys.argv
if len(args)-1 < 3 :
	print("use the command below to create program structure\nDirectory path should be relative\nLanguague can be comma sperated\n\npython3 createProgram \"directory\" \"filename\" \"language\"")
	exit()

print("Creating program folder structure ...\n")

extensions = {'C':'.c','PYTHON':'.py','py':'.py','C++':'.cpp',"JAVA":'.java'}

def createFile(filepath,message="#code goes below"):
	with open(filepath,'w') as f:
		print("created file :",filepath)
		f.write(message)



def createProgramFileStructure(directory,programName,language="C"):
	programDirectory = os.path.join(pwd,directory,programName)
	subDirs = os.path.split(directory)
	langDir = os.path.join(programDirectory,'language')
	language = [  l.strip() for l in language.split(",")]
	langs = [ os.path.join(programDirectory,'language',lang.lower())  for lang in language]
	langFiles = [ os.path.join( programDirectory,'language',lang.lower(),programName+extensions.get(lang.upper(),"."+lang.lower()) )  for lang in language]
	questionDir = os.path.join(programDirectory,'question')
	questionFile = os.path.join(programDirectory,'question',programName+".txt")
	testCasedir = os.path.join(programDirectory,'testcases')
	testCaseFile = os.path.join(programDirectory,'testcases',"sampledata")
	if not os.path.exists(programDirectory):
		try:
			os.makedirs(programDirectory)
			os.mkdir(questionDir)
			print("created question dir :",questionDir)
			createFile(questionFile,'#Write well documented question')
			os.mkdir(testCasedir)
			print("created testcase dir :",testCasedir)
			createFile(testCaseFile,"")
			os.mkdir(langDir)
			for lang in langs:
				os.mkdir(lang)
				print("created language dir :",lang)


			for lf in langFiles:
				createFile(lf)


		except Exception as err:
			print(err)
	else:
		print(programDirectory," -- already exists")



if __name__ == '__main__':
	createProgramFileStructure(args[1],args[2],args[3])