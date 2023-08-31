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
        
        argNames = list(map(lambda n: Name(id=n, ctx=Load()), argList))
        argNames = [Constant(value=transformedNode.name),
                    List(elts=argNames, ctx=Load())]
        
        
        before = Expr(value=Call(
                            func=Attribute(
                                value=Name(id='Profiler', ctx=Load()),
                                attr='record_start',
                                ctx=Load()),
                                args=argNames,
                                keywords=[]))       
        
        if isinstance(transformedNode.body, list):
            transformedNode.body.insert(0, before)
        else:
            transformedNode.body = [before, node.body]

        after = Expr(value=Call(
                            func=Attribute(
                                value=Name(id='Profiler', ctx=Load()),
                                attr='record_end',
                                ctx=Load()),
                                args=[Constant(value=transformedNode.name)],
                                keywords=[]))
        
        if isinstance(transformedNode.body[-1],Return):
            transformedNode.body.insert(-1, after)
        else:
            transformedNode.body.append(after)
        
        fix_missing_locations(transformedNode)
        
        return transformedNode

