from ast import *
from core.rewriter import rewrite
from core.transformers import RewriterCommand
from core.util import *
from pathlib import Path
import os
import sys


args = sys.argv
if len(args) < 3:
    print("Incomplete Command")

targetFile = sys.argv[2]
path = Path(targetFile)
fileContent = open(targetFile).read()

if not path.is_file():
    print("File not exists")

commandName = sys.argv[1]
cmds = select(lambda cmd: commandName in cmd.name(), RewriterCommand.__subclasses__())

if len(cmds) < 1:
    print("Rule not found")


if len(cmds) < 1:
    print("Command not found")

output = rewrite(cmds[0], fileContent)
print(output)
