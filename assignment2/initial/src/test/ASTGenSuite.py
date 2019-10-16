import unittest
from TestUtils import TestAST
from AST import *
class ASTGenSuite(unittest.TestCase):
    def test_00(self):
        """Simple program: int main() {} """
        input = """int a,c,d[2];"""
        expect = str(Program([VarDecl('a',IntType()),VarDecl('c',IntType()),VarDecl('d',ArrayType(2,IntType()))]))
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
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('a',FloatType()),VarDecl('b',ArrayPointerType(IntType()))],IntType(),Block([VarDecl('a',IntType()),Continue(),Break(),Return()])),VarDecl('foo',ArrayType(3,IntType())),FuncDecl(Id('foo'),[VarDecl('c',ArrayPointerType(IntType()))],FloatType(),Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_02(self):
        """More complex program"""
        input = """string c;
            """
        expect = str(Program([VarDecl('c',StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_03(self):
        """More complex program"""
        input = """
int a[3];
boolean foo(){
    a[2] = c;
}

            """
        expect = str(Program([VarDecl('a',ArrayType(3,IntType())),FuncDecl(Id('foo'),[],BoolType(),Block([BinaryOp('=',ArrayCell(Id('a'),IntLiteral(2)),Id('c'))]))]))
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

    def test_06(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
            [CallExpr(Id("putIntLn"), [IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_07(self):
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program(
            [FuncDecl(Id("main"), [], IntType(), Block([CallExpr(Id("getIntLn"), [])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    def test_08(self):
        input = """int abc[10],a,b;"""
        expect = str(Program([VarDecl("abc", ArrayType(10, IntType())), VarDecl(
            "a", IntType()), VarDecl("b", IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))
    def test_11(self):
        input = """int abc[10],a,b;"""
        expect = str(Program([VarDecl("abc", ArrayType(10, IntType())), VarDecl(
            "a", IntType()), VarDecl("b", IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_12(self):
        input = """int abc[10],a,b;
        void main() {}
        """
        expect = str(Program([VarDecl("abc", ArrayType(10, IntType())), VarDecl("a", IntType(
        )), VarDecl("b", IntType()), FuncDecl(Id("main"), [], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_13(self):
        input = """
        int abc[10],a,b;
        void main() {
            foo()/1e3*k&&true;
        }
        """
        expect = str(Program([VarDecl('abc',ArrayType(10,IntType())),VarDecl('a',IntType(
            )),VarDecl('b',IntType()),FuncDecl(Id('main'),[],VoidType(
            ),Block([BinaryOp('&&',BinaryOp('*',BinaryOp('/',CallExpr(Id('foo'),[]),FloatLiteral(1000.0)),Id('k')),BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_14(self):
        input = """void main(string arg[]){foo(a,c);}"""
        expect = str(Program([FuncDecl(Id('main'), [VarDecl('arg', ArrayPointerType(
            StringType()))], VoidType(), Block([CallExpr(Id('foo'), [Id('a'), Id('c')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_15(self):
        input = """void main(string arg[]){int b,c,d;}"""
        expect = str(Program([FuncDecl(Id('main'), [VarDecl('arg', ArrayPointerType(StringType()))], VoidType(
        ), Block([VarDecl('b', IntType()), VarDecl('c', IntType()), VarDecl('d', IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_16(self):
        input = """int a;"""
        expect = str(Program([VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_17(self):
        input = """int a[10];"""
        expect = str(Program([VarDecl("a",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_18(self):
        input = """void main(string arg[]) {

        }
        int foo(boolean a,int b[]) {

        }"""
        expect = str(Program([FuncDecl(Id('main'), [VarDecl('arg', ArrayPointerType(StringType()))], VoidType(), Block(
            [])), FuncDecl(Id('foo'), [VarDecl('a',BoolType()),VarDecl('b',ArrayPointerType(IntType()))], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_19(self):
        input = """void main() {
            boolean a[5];
        }"""
        expect = str(Program(
            [FuncDecl(Id("main"), [], VoidType(), Block([VarDecl("a", ArrayType(5,BoolType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_20(self):
        input = """void main() {
            string a;
        }"""
        expect = str(Program(
            [FuncDecl(Id("main"), [], VoidType(), Block([VarDecl("a", StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_21(self):
        input = """void main() {
            float a;
        }"""
        expect = str(Program(
            [FuncDecl(Id("main"), [], VoidType(), Block([VarDecl("a", FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

