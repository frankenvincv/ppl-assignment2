import unittest
from TestUtils import TestAST
from AST import *
class ASTGenSuite(unittest.TestCase):
    def test_00(self):
        """Simple program: int main() {} """
        input = """int a,c,d[2];"""
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('d'),ArrayType(2,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_01(self):
        """More complex program"""
        input = """
int main(float a,int b[]){
    int a;
    continue;
    break;
    return;
}
int foo[3];
float foo(int c[]){
    continue;
}
        """
        expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType()),VarDecl(Id('b'),ArrayPointerType(IntType()))],IntType(),Block([VarDecl(Id('a'),IntType()),Continue(),Break(),Return()])),VarDecl(Id('foo'),ArrayType(3,IntType())),FuncDecl(Id('foo'),[VarDecl(Id('c'),ArrayPointerType(IntType()))],FloatType(),Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_02(self):
        """More complex program"""
        input = """string c;
            """
        expect = str(Program([VarDecl(Id('c'),StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_03(self):
        """More complex program"""
        input = """
int a[3];
boolean foo(){
    a[] = c;
}

            """
        expect = str(Program([VarDecl(Id('a'),ArrayType(3,IntType())),FuncDecl(Id('foo'),[],BoolType(),Block([BinaryOp('=',UnaryOp('[]',Id('a')),Id('c'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_04(self):
        input = """
boolean[] func() {
    a[2] + 4 == 2;
}
        """
        expect = str(Program([FuncDecl(Id('func'),[],ArrayPointerType(BoolType()),Block([BinaryOp('==',BinaryOp('+',ArrayCell(Id('a'),IntLiteral(2)),IntLiteral(4)),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))
    def test_05(self):
        input = """
boolean[] func() {
    "2x+3y" == foo(x+3)[y != 3];
}
        """
        expect = str(Program([FuncDecl(Id('func'),[],ArrayPointerType(BoolType()),Block([BinaryOp('==',StringLiteral('2x+3y'),ArrayCell(CallExpr(Id('foo'),[BinaryOp('+',Id('x'),IntLiteral(3))]),BinaryOp('!=',Id('y'),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))