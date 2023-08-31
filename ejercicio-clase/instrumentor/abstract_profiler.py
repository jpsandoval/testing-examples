from function_instrumentor import *
import threading

# Clase que representa la estructura de un profiler
class AbstractProfiler:
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    # Usamos un singleton para no crear instancias a cada rato
    @classmethod
    def getInstance(cls):
        with cls.__singleton_lock:
            if not cls.__singleton_instance:
                cls.__singleton_instance = cls()
        return cls.__singleton_instance

    # Al resetear actualizamos la instancia de singleton a None
    @classmethod
    def reset(cls):
        cls.__singleton_instance = None

    # Este metodo se llama cada vez se ejecuta una funcion
    @classmethod
    def record_start(cls, functionName,args):
        print("entrando")
        cls.getInstance().fun_call_start(functionName,args)

    @classmethod
    def record_end(cls, value):
        cls.getInstance().fun_call_end(value)

    def fun_call_start(self,functionName,args):
        pass
    
    def fun_call_end(self,value):
        pass

    # recibe un archivo que contiene un programa
    # lo instrumenta y lo ejecuta recolectando datos en el profiler
    # devuelve el objeto profiler con los datos
    @classmethod
    def profile(cls,fileName):
        cls.reset()
        instance = cls.getInstance()
        ast = cls.get_ast_from_file(fileName)
        newAst = cls.instrument(ast)
        print(unparse(newAst))
        print("Ejecutando")
        exec(compile(newAst, filename="<ast>", mode ="exec"), locals(), locals())
        return instance
    
    # Este metodo injecta codigo al inicio de cada funcion en el programa
    @classmethod
    def instrument(cls,ast):
        visitor = FunctionInstrumentor()
        return  fix_missing_locations(visitor.visit(ast))
    
    # recupera el AST dado un archivo
    @classmethod
    def get_ast_from_file(cls, fileName):
        file = open(fileName)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)
        return tree
    
    