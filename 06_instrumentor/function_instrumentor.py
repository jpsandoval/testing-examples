from ast import *

# Clase que permite inyectar codigo de tal forma que podamos reportar que funciones se ejecutan
class FunctionInstrumentor(NodeTransformer):
    
    def visit_Module(self, node: Module):
        transformedNode = NodeTransformer.generic_visit(self, node)
        import_profile_injected = parse("from profiler import Profiler")
        transformedNode.body.insert(0, import_profile_injected.body[0])
        fix_missing_locations(transformedNode)

        return transformedNode

    def visit_FunctionDef(self, node: FunctionDef):
        transformedNode = NodeTransformer.generic_visit(self, node)
        
        # Inyectamos codigo para llamar al profiler en la primera linea de la definicion de una funcion
        argList = list(map(lambda x: x.arg, transformedNode.args.args))
        injectedCode = parse('Profiler.record(\''+
        transformedNode.name + '\',[' + ", ".join(argList) + '])')
    
        if isinstance(transformedNode.body, list):
            transformedNode.body.insert(0, injectedCode.body[0])
        else:
            transformedNode.body = [injectedCode.body[0], node.body]

        fix_missing_locations(transformedNode)
        
        return transformedNode

