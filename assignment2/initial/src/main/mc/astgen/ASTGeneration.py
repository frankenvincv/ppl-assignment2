from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        declList = []
        for x in ctx.declarates():
            decl = self.visitDeclarates(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)


    # Visit a parse tree produced by MCParser#declarates.
    def visitDeclarates(self, ctx:MCParser.DeclaratesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_declarate.
    def visitVar_declarate(self, ctx:MCParser.Var_declarateContext):
        varDec = []
        varType = self.visit(ctx.primitive_type())
        for x in ctx.var():
            var = self.visitVar(x)
            if( isinstance(var,list)):
                varDec.append(VarDecl(var[0],ArrayType(var[1],varType)))
            else:
                varDec.append(VarDecl(var,varType))
        return varDec


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        if ctx.INT(): return IntType()
        if ctx.FLOAT(): return FloatType()
        if ctx.STRING(): return StringType()
        if ctx.BOOLEAN(): return BoolType()


    # Visit a parse tree produced by MCParser#var_list.


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        if ctx.LSB():
            return [ctx.ID().getText(),int(ctx.INTLIT().getText())]
        return ctx.ID().getText()


    def visitFunc_declarate(self, ctx:MCParser.Func_declarateContext):
        name = Id(ctx.ID().getText())
        returnType = self.visit(ctx.func_type())
        paraList = []
        if (ctx.para()):
            for x in ctx.para():
                para = self.visitPara(x)
                if isinstance(para, list): paraList.extend(para if para else [])
                else: paraList.append(para)
            return FuncDecl(name,paraList,returnType,self.visit(ctx.block_statement()))
        else: return FuncDecl(name,paraList,returnType,self.visit(ctx.block_statement()))






    # Visit a parse tree produced by MCParser#func_type.
    def visitFunc_type(self, ctx:MCParser.Func_typeContext):
        if ctx.VOID(): return VoidType()
        if ctx.primitive_type(): return self.visit(ctx.primitive_type())
        if ctx.array_pointer_type(): return self.visit(ctx.array_pointer_type())
    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        Arraytype = self.visit(ctx.primitive_type())
        return ArrayPointerType(Arraytype)  


    # Visit a parse tree produced by MCParser#para.
    def visitPara(self, ctx:MCParser.ParaContext):
        paraType = self.visit(ctx.primitive_type())
        return VarDecl(ctx.ID().getText(),ArrayPointerType(paraType)) if (ctx.LSB()) else VarDecl(ctx.ID().getText(),paraType)


# Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        expr = self.visit(ctx.exp)
        thenStmt = self.visit(ctx.statement())
        return If(expr,thenStmt,self.visit(ctx.else_statement())) if (ctx.else_statement()) else If(exp,thenStmt)




    # Visit a parse tree produced by MCParser#else_statement.
    def visitElse_statement(self, ctx:MCParser.Else_statementContext):
        return self.visit(ctx.statement())


    # Visit a parse tree produced by MCParser#do_while_statement.
    def visitDo_while_statement(self, ctx:MCParser.Do_while_statementContext):
        expr = self.visit(ctx.exp)
        sl = []
        for x in ctx.statement():
            stmt = self.visitStatement(x)
            sl.append(stml)
        return Dowhile(sl,expr)


    # Visit a parse tree produced by MCParser#for_statement.
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        loopStmt = self.visit(ctx.statement())
        return For(expr1,expr2,expr3,loopStmt)


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by MCParser#return_statement.
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        if (ctx.exp()):
            return Return(self.visit(exp()))
        else: return Return()


    # Visit a parse tree produced by MCParser#exp_statement.
    def visitExp_statement(self, ctx:MCParser.Exp_statementContext):
        return self.visit(ctx.exp())


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        memberList = []
        for x in ctx.stmt_vardecl():
            member = self.visitStmt_vardecl(x)
            if isinstance(member, list): memberList.extend(member if member else [])
            else: memberList.append(member)
        return Block(memberList)


    # Visit a parse tree produced by MCParser#stmt_vardect.
    def visitStmt_vardecl(self, ctx:MCParser.Stmt_vardeclContext):
        return self.visit(ctx.statement()) if (ctx.statement()) else self.visit(ctx.var_declarate())

    # Visit a parse tree produced by MCParser#literals.
    def visitLiterals(self, ctx:MCParser.LiteralsContext):
        if (ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        if (ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if (ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT().getText())
        if (ctx.boolean_literals()):
            return self.visit(ctx.boolean_literals())

    # Visit a parse tree produced by MCParser#boolean_literals.
    def visitBoolean_literals(self, ctx:MCParser.Boolean_literalsContext):
        val = True if ctx.TRUE() else False
        return BooleanLiteral(val)

    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp1())
        left = self.visit(ctx.exp1())
        right = self.visit(ctx.exp())
        op = ctx.ASSIGN().getText()
        return BinaryOp(op,left,right)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp2())
        left = self.visit(ctx.exp1())
        right = self.visit(ctx.exp2())
        op = ctx.OR().getText()
        return BinaryOp(op,left,right)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp3())
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        op = ctx.AND().getText()
        return BinaryOp(op,left,right)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp4(0))
        left = self.visit(ctx.exp4(0))
        right = self.visit(ctx.exp4(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp5(0))
        left = self.visit(ctx.exp5(0))
        right = self.visit(ctx.exp5(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp6())
        left = self.visit(ctx.exp5())
        right = self.visit(ctx.exp6())
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp7())
        left = self.visit(ctx.exp6())
        right = self.visit(ctx.exp7())
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp8())
        body = self.visit(ctx.exp7())
        op = ctx.getChild(0).getText()
        return UnaryOp(op,body)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visit(ctx.operand())


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        if (ctx.literals()):
            return self.visit(ctx.literals())
        if (ctx.ID()):
            return Id(ctx.ID().getText())
        if (ctx.func_call()):
            return self.visit(ctx.func_call())
        if (ctx.sub_exp()):
            return self.visit(ctx.sub_exp())
        return self.visit(ctx.index_exp())


    # Visit a parse tree produced by MCParser#sub_exp.
    def visitSub_exp(self, ctx:MCParser.Sub_expContext):
        return self.visit(ctx.exp())

    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        method = Id(ctx.ID().getText())
        paraList = []
        for x in ctx.exp():
            para = self.visitExp(x)
            if isinstance(para, list): paraList.extend(para if para else [])
            else: paraList.append(para)
        return CallExpr(method,paraList)
        

    # Visit a parse tree produced by MCParser#index_exp.
    def visitIndex_exp(self, ctx:MCParser.Index_expContext):
        if (ctx.ID()):
            arr = Id(ctx.ID().getText())
        else: arr = self.visit(ctx.func_call())
        idx = self.visit(ctx.exp())
        return ArrayCell(arr,idx)