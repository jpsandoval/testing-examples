from core.util import *
from core.rules import *
from pathlib import Path
import sys

args = sys.argv
if len(args) < 3:
    print("Incomplete Command")

targetFile = sys.argv[2]
path = Path(targetFile)
fileContent = open(targetFile).read()

if not path.is_file():
    print("File not exists")

ruleName = sys.argv[1]
print(EvalUsedRule.name())

rules = select(lambda rule: ruleName in rule.name(), Rule.__subclasses__())

if len(rules) < 1:
    print("Rule not found")

warnings = analyze(rules[0], fileContent)

for wrn in warnings:
    print(wrn)
