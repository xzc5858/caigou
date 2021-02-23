import os
import sys

scriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
ls = open(scriptPath + '/list.txt', 'a', encoding="utf-8")
detail = open(scriptPath + '/detail.txt', 'w', encoding="utf-8")
