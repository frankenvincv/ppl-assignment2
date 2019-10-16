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
    def test_program_22(self):
        input = """
void main(){}
                """
        expect=str(Program([FuncDecl(Id('main'),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_program_23(self):
        input = """
int a,a[2],b;float x,_x[3],y;boolean k,_k[4],h;
                """
        expect= str(Program([VarDecl('a',IntType()),VarDecl('a',ArrayType(2,IntType())),VarDecl('b',IntType()),VarDecl('x',FloatType(
            )),VarDecl('_x',ArrayType(3,FloatType())),VarDecl('y',FloatType()),VarDecl('k',BoolType(
            )),VarDecl('_k',ArrayType(4,BoolType())),VarDecl('h',BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_program_24(self):
        input = """
void a(){void b(){}}
                """
        expect=str(Program([FuncDecl(Id('a'),[],VoidType(),Block([CallExpr(Id('b'),[]),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_program_25(self):
        input = """
void _a(){
    if (a==b) return a;
}
                """
        expect=str(Program([FuncDecl(Id('_a'),[],VoidType(),Block([
            If(BinaryOp('==',Id('a'),Id('b')),Return(Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_program_26(self):
        input = """int main(){
            do {} while 1;
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
            [Dowhile([Block([])], IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_program_27(self):
        input = """int main(){
            do {
                int a;
            } {
                float b[2];
            }{
                foo(x==3)[2];
            } while 1;
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
            [Dowhile([Block([VarDecl('a',IntType())]),Block([VarDecl('b',ArrayType(2,FloatType()))]),
                Block([ArrayCell(CallExpr(Id('foo'),[BinaryOp('==',Id('x'),IntLiteral(3))]),IntLiteral(2))])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_program_28(self):
        input = """void main() {
                      int i;
                      for(a;b;c)d;
                      } 
                """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),For(Id('a'),Id('b'),Id('c'),Id('d'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_program_29(self):
        input = """void main() {
                      int i;
                      for( a = 0 ; a < 10 ; a + 1 ) {
                         if(a == 1) break;
                        }
                      } """
        expect=str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),For(BinaryOp('=',Id('a'),IntLiteral(0)),
            BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([If(BinaryOp('==',Id('a'),IntLiteral(1)),Break())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_program_30(self):
        input = """
void _a(float a,int k){if(a)if(b)if(c)if(d)if(e){for(f;g;h)a;}else(e);}
                """
        expect=str(Program([FuncDecl(Id('_a'),[VarDecl('a',FloatType()),VarDecl('k',IntType())],VoidType()
            ,Block([If(Id('a'),If(Id('b'),If(Id('c'),If(Id('d'),If(Id('e'),Block([For(Id('f'),Id('g'),Id('h'),Id('a'))]),Id('e'))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
#     def test_program_31(self):
#         input = """
# void _a(float a,int k){if(a)if(b)if(c)if(d)if(e){for(f;g;h)a;}else(e);}
# float[] _c(string a[]){for(i=0;i<100;i=i+1){for(j=0;j<100;i=i+1)return;}}
# string _d(int a[],float b){do{if(a)for(b;c;d)return;}while(true);}
# boolean[] _e(boolean k,boolean j[5]){/*do no thing*/} 
#                 """
#         expect="Error on line 5 col 33: 5"
#         self.assertTrue(TestAST.checkASTGen(input,expect,251))
#     def test_program_32(self):
#         input = """
# void _a(float a,int k){if(a)if(b)if(c)if(d)if(e){for(f;g;h)a;}else(e);}
# float[] _c(string a[]){for(i=0;i<100;i=i+1){for(j=0;j<100;i=i+1)return;}}
# string _d(int a[],float b){do{if(a)for(b;c;d)return;}while(true);}
# boolean[] _e(boolean k,boolean j[]){_a(.2e-12,32);_c("testpara");_d(x[],3.e-12);} 
#                 """
#         expect=str()
#         self.assertTrue(TestAST.checkASTGen(input,expect,252))
#     def test_program_33(self):
#         input = """
# boolean isTrue(boolean k){if(k==true)return true;else return false;}
#                 """
#         expect=str()
#         self.assertTrue(TestAST.checkASTGen(input,expect,253))
#     def test_program_34(self):
#         input = """
# string isString(string str){if(s="ppl")return("p");else if(s="dsa")return("d");else return("nothing");}
#                 """
#         expect=str()
#         self.assertTrue(TestAST.checkASTGen(input,expect,254))
#     def test_program_35(self):
#         input = """
# boolean isTrue(boolean k){if(k==true)return true;else return false;}
# string isString(string str){if(s="ppl")return("p");else if(s="dsa")return("d");else return("nothing");}
# void main(){int a; a = 1; printf(isTrue(a)||isString(a));}
#                 """
#         expect=str()
#         self.assertTrue(TestAST.checkASTGen(input,expect,255))
#     def test_program_36(self):
#         input = """
# boolean isPrime;
# int checkPrime(int index){for(i = 2; i <=index/2;i = i+1){if(index%i==0){return 0;}}return 1;}
#                 """
#         expect=str()
#         self.assertTrue(TestAST.checkASTGen(input,expect,256))
#     def test_program_37(self):
#         input = """
# boolean isTrue(boolean k){if(k==true)return true;else return false;}
# string isString(string str){if(s="ppl")return("p");else if(s="dsa")return("d");else return("nothing");}
# boolean isPrime;
# int checkPrime(int index){for(i = 2; i <=index/2;i = i+1){if(index%i==0){return 0;}}return 1;}
# void main(){int a; a = 1; printf(isTrue(a)||isString(a)||checkPrime(3));}
#                 """
#         expect=str()
#         self.assertTrue(TestAST.checkASTGen(input,expect,257))
#     def test_program_38(self):
#         input = """
# int a[5];
# void init(){for(i=0;i<5;i=i+1)a[i]=i;}
#                 """
#         expect=str()
#         self.assertTrue(TestAST.checkASTGen(input,expect,258))
#     def test_program_39(self):
#         input = """
# int a[5];
# void init(){for(i=0;i<5;i=i+1)a[i]=i;}
# int main(int argc, string argv){init();for(i=0;i<5;i=i+1){printf("%d : \t",a[i]);}}
#                 """
#         expect="%d : "
#         self.assertTrue(TestAST.checkASTGen(input,expect,259))
