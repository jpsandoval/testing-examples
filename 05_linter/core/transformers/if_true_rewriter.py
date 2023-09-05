from _ast import If
from ast import *
import ast
from typing import Any
from core.rewriter import RewriterCommand


class IfTrueTransformer(NodeTransformer):
    def visit_If(self, node: If):
        copy = NodeTransformer.generic_visit(self,node)
        match copy:
            case If(test= Constant(value=True),
                    body= true_body,
                    orelse= _):
                return true_body
            case _ :
              return copy


  


class IfTrueRewriterCommand(RewriterCommand):
    
    def apply(self, tree):
        visitor = IfTrueTransformer()
        new_tree = visitor.visit(tree)
        new_tree = fix_missing_locations(new_tree)
        return new_tree
    
    @classmethod
    def name(self):
        return 'eval'