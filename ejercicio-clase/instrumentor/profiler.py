
# Clase que rastrea y reporta las funciones que se ejecutan
from abstract_profiler import AbstractProfiler


class Profiler(AbstractProfiler):

    # Metodos de instancia
    def __init__(self):
        self.functions_called = []
    
    # metodo se llama cada vez que se ejecuta una funcion    
    def fun_call_start(self, functionName, args):
        print("entrando: "+functionName)
        self.functions_called.append((functionName, args))
    
    def fun_call_end(self,functionName):
        print("saliendo: "+functionName)

    def report_executed_functions(self):
        output = []
        output.append("-- Executed functions --")
        for (fun, args) in self.functions_called:
            if len(args) != 0:
                output.append(("Function " + fun + " with arguments " + " ".join(str(arg) for arg in args)))
            else:
                output.append(("Function " + fun + " with no arguments."))
        return '\n'.join(output)

