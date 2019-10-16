# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declarates.
    def visitDeclarates(self, ctx:MCParser.DeclaratesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_declarate.
    def visitVar_declarate(self, ctx:MCParser.Var_declarateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_declarate.
    def visitFunc_declarate(self, ctx:MCParser.Func_declarateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_type.
    def visitFunc_type(self, ctx:MCParser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para.
    def visitPara(self, ctx:MCParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#else_statement.
    def visitElse_statement(self, ctx:MCParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_statement.
    def visitDo_while_statement(self, ctx:MCParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_statement.
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_statement.
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_statement.
    def visitExp_statement(self, ctx:MCParser.Exp_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt_vardecl.
    def visitStmt_vardecl(self, ctx:MCParser.Stmt_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literals.
    def visitLiterals(self, ctx:MCParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#boolean_literals.
    def visitBoolean_literals(self, ctx:MCParser.Boolean_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#sub_exp.
    def visitSub_exp(self, ctx:MCParser.Sub_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#index_exp.
    def visitIndex_exp(self, ctx:MCParser.Index_expContext):
        return self.visitChildren(ctx)



del MCParser