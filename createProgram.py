#!/usr/bin/python3
#version 1.1.0

import os
import sys


pwd = os.getcwd()
args = sys.argv
if len(args)-1 < 2 :
	print("use the command below to create program structure\nDirectory path should be relative\n\npython3 createProgram \"directory\" \"filename\"")
	exit()

print("Creating program folder structure ...\n")

extensions = {'C':'.c','PYTHON':'.py','py':'.py','C++':'.cpp',"JAVA":'.java'}

c="""

#include <stdio.h>

int main(void) {
	// your code goes here
	return 0;
}

"""

py="""

#start writing code down

"""

java="""

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class CodeForLife
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
	}
}


"""

cpp="""

#include <iostream>
using namespace std;

int main() {
	// your code goes here
	return 0;
}

"""

snippets = {"c":c,'py':py,'java':java,'cpp':cpp}


def createFile(filepath,message="#code goes below"):
	exten = filepath.split(".")[-1]
	snippet = snippets.get(exten, message)
	with open(filepath,'w') as f:
		print("created file :",filepath)
		f.write(snippet)



def createProgramFileStructure(directory,programName,language="C,c++,python,java"):
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
	createProgramFileStructure(args[1],args[2])