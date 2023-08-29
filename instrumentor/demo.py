from profiler import *

profiler = Profiler.profile("input_code/code2.py")
result = profiler.report_executed_functions()
print(result)