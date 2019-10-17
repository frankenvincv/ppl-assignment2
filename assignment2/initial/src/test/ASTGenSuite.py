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
    def test_09(self):
        input = """float abc[10],a,b;"""
        expect = str(Program([VarDecl("abc", ArrayType(10, FloatType())), VarDecl(
            "a", FloatType()), VarDecl("b", FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
    def test_10(self):
        input = """boolean abc[10],a,b;"""
        expect = str(Program([VarDecl("abc", ArrayType(10, BoolType())), VarDecl(
            "a", BoolType()), VarDecl("b", BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

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
    def test_program_31(self):
        input = """
void _a(float a,int k){if(a)if(b)if(c)if(d)if(e){for(f;g;h)a;}else(e);}
float[] _c(string a[]){for(i=0;i<100;i=i+1){for(j=0;j<100;i=i+1)return;}}
                """
        expect=str(Program([FuncDecl(Id('_a'),[VarDecl('a',FloatType()),VarDecl('k',IntType())],VoidType()
            ,Block([If(Id('a'),If(Id('b'),If(Id('c'),If(Id('d'),If(Id('e'),Block([For(Id('f'),Id('g'),Id('h'),Id('a'))]),Id('e'))))))])),
        FuncDecl(Id('_c'),[VarDecl('a',ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),
                BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                Block([For(BinaryOp('=',Id('j'),IntLiteral(0)),BinaryOp('<',Id('j'),IntLiteral(100)),
                BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Return())]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_program_32(self):
            input = """
void _a(float a,int k){if(a)if(b)if(c)if(d)if(e){for(f;g;h)a;}else(e);}
float[] _c(string a[]){for(i=0;i<100;i=i+1){for(j=0;j<100;i=i+1)return;}}
string _d(int a[],float b){do{if(a)for(b;c;d)return;}while(true);}
boolean[] _e(boolean k,boolean j[]){_a(.2e-12,32);_c("testpara");_d(x[],3.e-12);} 
                    """
            expect = str(Program([FuncDecl(Id('_a'),[VarDecl('a',FloatType()),VarDecl('k',IntType())],VoidType()
                ,Block([If(Id('a'),If(Id('b'),If(Id('c'),If(Id('d'),If(Id('e'),Block([For(Id('f'),Id('g'),Id('h'),Id('a'))]),Id('e'))))))])),
                FuncDecl(Id('_c'),[VarDecl('a',ArrayPointerType(StringType()))],ArrayPointerType(FloatType()),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),
                BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                Block([For(BinaryOp('=',Id('j'),IntLiteral(0)),BinaryOp('<',Id('j'),IntLiteral(100)),
                BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Return())]))])),
                FuncDecl(Id('_d'),[VarDecl('a',ArrayPointerType(IntType())),VarDecl('b',FloatType())],StringType(),
                Block([Dowhile([Block([If(Id('a'),For(Id('b'),Id('c'),Id('d'),Return()))])],BooleanLiteral(True))])),FuncDecl(Id('_e'),
                [VarDecl('k',BoolType()),VarDecl('j',ArrayPointerType(BoolType()))],ArrayPointerType(BoolType()),
                Block([CallExpr(Id('_a'),[FloatLiteral(2e-13),IntLiteral(32)]),CallExpr(Id('_c'),[StringLiteral('testpara')]),
                CallExpr(Id('_d'),[Id('x'),FloatLiteral(3e-12)])]))
                ]))
            self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_program33(self):
        input = """int main(){
            float a,b[5],c[10];
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl("a", FloatType(
        )), VarDecl("b", ArrayType(5, FloatType())), VarDecl("c", ArrayType(10, FloatType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_program34(self):
        input = """void main(int a,string b[],boolean c,float d){

        }"""
        expect = str(Program([FuncDecl(Id("main"), [VarDecl("a", IntType()), VarDecl("b", ArrayPointerType(
            StringType())), VarDecl("c", BoolType()), VarDecl("d", FloatType())], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_program35(self):
        input = """int main(){
            int a;
            float b;
            boolean c[2];
            string d;
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([VarDecl("a", IntType()), VarDecl(
            "b", FloatType()), VarDecl("c", ArrayType(2, BoolType())), VarDecl("d", StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_program36(self):
        input = """int main(){
            if (a==b) {}
        }"""
        expect = str(
            Program([FuncDecl(Id('main'), [], IntType(), Block([If(BinaryOp('==',Id('a'),Id('b')), Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_program37(self):
        input = """int main(){
            if (a==b) {}
            else {return b;}
        }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),
            Block([If(BinaryOp('==',Id('a'),Id('b')),Block([]),Block([Return(Id('b'))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_program38(self):
        input = """int main(){
            do {} while true;
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
            [Dowhile([Block([])], BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_program39(self):
        input = """int main(){
            do {} {} while true;
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
            [Dowhile([Block([]), Block([])], BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_program40(self):
        input = """int main(){
            for (i=1;i<1;i=i+1) {}
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([For(BinaryOp("=", Id("i"), IntLiteral(1)), BinaryOp(
            "<", Id("i"), IntLiteral(1)), BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))), Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_program41(self):
        input = """int main(){
            break;
        }"""
        expect = str(
            Program([FuncDecl(Id("main"), [], IntType(), Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_program42(self):
        input = """int main(){
            continue;
        }"""
        expect = str(
            Program([FuncDecl(Id("main"), [], IntType(), Block([Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_program43(self):
        input = """int main(){
            return;
        }"""
        expect = str(
            Program([FuncDecl(Id("main"), [], IntType(), Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_program44(self):
        input = """int main(){
            return false;
        }"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block(
            [Return(BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))
    def test_program45(self):
        input = """void main(int argc, string argv[]){
            abc = def;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp("=", Id("abc"), Id("def"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_program46(self):
        input = """void main(int argc, string argv[]){
            abc||def;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp("||", Id("abc"), Id("def"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_program47(self):
        input = """void main(int argc, string argv[]){
            mam&&coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp("&&", Id("mam"), Id("coi"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_program48(self):
        input = """void main(int argc, string argv[]){
            mam==coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp("==", Id("mam"), Id("coi"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_program49(self):
        input = """void main(int argc, string argv[]){
            abc!=def;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp("!=", Id("abc"), Id("def"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_program50(self):
        input = """void main(int argc, string argv[]){
            mam<coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp("<", Id("mam"), Id("coi"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_program51(self):
        input = """void main(int argc, string argv[]){
            coi>mam;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp(">", Id("coi"), Id("mam"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_program52(self):
        input = """void main(int argc, string argv[]){
            coi>=mam;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp(">=", Id("coi"), Id("mam"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_program53(self):
        input = """void main(int argc, string argv[]){
            mam<=coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp("<=", Id("mam"), Id("coi"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_program54(self):
        input = """void main(int argc, string argv[]){
            coi+mam = mam+coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp('=',BinaryOp('+',Id('coi'),Id('mam')),BinaryOp('+',Id('mam'),Id('coi')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_program55(self):
        input = """void main(int argc, string argv[]){
            coi-mam=mam-coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp('=',BinaryOp('-',Id('coi'),Id('mam')),BinaryOp('-',Id('mam'),Id('coi')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_program56(self):
        input = """void main(int argc, string argv[]){
            coi/mam=mam/coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp('=',BinaryOp('/',Id('coi'),Id('mam')),BinaryOp('/',Id('mam'),Id('coi')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_program57(self):
        input = """void main(int argc, string argv[]){
            coi*mam=mam*coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp('=',BinaryOp('*',Id('coi'),Id('mam')),BinaryOp('*',Id('mam'),Id('coi')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_program58(self):
        input = """void main(int argc, string argv[]){
            coi%mam=mam%coi;
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp('=',BinaryOp('%',Id('coi'),Id('mam')),BinaryOp('%',Id('mam'),Id('coi')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_program59(self):
        input = """void main(int argc, string argv[]){
            -so;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([UnaryOp("-", Id("so"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_program60(self):
        input = """void main(int argc, string argv[]){
            !so;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([UnaryOp("!", Id("so"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_program61(self):
        input = """void main(int argc, string argv[]){
            so[x=3];
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([ArrayCell(Id("so"), BinaryOp('=',Id('x'),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_program62(self):
        input = """void main(int argc, string argv[]){
            a*(b+c);
        }"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(), 
            Block([BinaryOp("*", Id("a"), BinaryOp("+", Id("b"), Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_program63(self):
        input = """void main(int argc, string argv[]){
            1;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([IntLiteral(1)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_program64(self):
        input = """void main(int argc, string argv[]){
            1.E-12;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([FloatLiteral(1.e-12)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_program65(self):
        input = """void main(int argc, string argv[]){
            1.24567;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([FloatLiteral(1.24567)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))
    def test_program66(self):
        input = """void main(int argc, string argv[]){
            1.24567e1;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([FloatLiteral(1.24567e1)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_program67(self):
        input = """void main(int argc, string argv[]){
            1.e12;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([FloatLiteral(1.e12)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_program68(self):
        input = """void main(int argc, string argv[]){
            ".2E-1";
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([StringLiteral(".2E-1")]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_program69(self):
        input = """void main(int argc, string argv[]){
            true;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BooleanLiteral(True)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_program70(self):
        input = """void main(int argc, string argv[]){
            false;
        }"""
        expect = str(
            Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BooleanLiteral(False)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_program71(self):
        input = """void main(int argc, string argv[]){
            foo();
        }"""
        expect = str(Program(
            [FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([CallExpr(Id("foo"), [])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_program72(self):
        input = """void main(int argc, string argv[]){
            foo(1,1.2,a,"2",true);
        }"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                    Block([CallExpr(Id("foo"), 
                    [IntLiteral(1), FloatLiteral(1.2), Id("a"), StringLiteral("2"), BooleanLiteral(True)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_program73(self):
        input = """void main(int argc, string argv[]){
            a+b*c[1]/d%f;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
                Block([BinaryOp("+", Id("a"), BinaryOp("%", BinaryOp("/", BinaryOp("*", Id("b"), ArrayCell(Id("c"), IntLiteral(1))), Id("d")), Id("f")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_program74(self):
        input = """void main(int argc, string argv[]){
            abc--bef;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
         Block([BinaryOp("-", Id("abc"), UnaryOp("-", Id("bef")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_program75(self):
        input = """void main(int argc, string argv[]){
            abc--!bef;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
         Block([BinaryOp("-", Id("abc"), UnaryOp("-", UnaryOp("!", Id("bef"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_program76(self):
        input = """void main(int argc, string argv[]){
            a == b != c >= d = e <= phu > f < g;
        }"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',ArrayPointerType(StringType()))],VoidType(),
            Block([BinaryOp('==',Id('a'),Id('b')),BinaryOp('=',BinaryOp('>=',Id('c'),Id('d')),BinaryOp('<=',Id('e'),Id('phu'))),BinaryOp('<',Id('f'),Id('g'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    def test_program77(self):
        input = """
string _d(int a[],float b){do{if(a)for(b;c;d)return;}while(true);}
boolean[] _e(boolean k,boolean j[]){_a(.2e-12,32);_c("testpara");_d(x[],3.e-12);} 
                """
        expect=str(Program([FuncDecl(Id('_d'),[VarDecl('a',ArrayPointerType(IntType())),VarDecl('b',FloatType())],StringType(),
                Block([Dowhile([Block([If(Id('a'),For(Id('b'),Id('c'),Id('d'),Return()))])],BooleanLiteral(True))])),FuncDecl(Id('_e'),
                [VarDecl('k',BoolType()),VarDecl('j',ArrayPointerType(BoolType()))],ArrayPointerType(BoolType()),
                Block([CallExpr(Id('_a'),[FloatLiteral(2e-13),IntLiteral(32)]),CallExpr(Id('_c'),[StringLiteral('testpara')]),
                CallExpr(Id('_d'),[Id('x'),FloatLiteral(3e-12)])]))
                ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_program78(self):
        input = """
boolean isTrue(boolean k){if(k==true)return true;else return false;}
                """
        expect=str(Program([FuncDecl(Id('isTrue'),[VarDecl('k',BoolType())],BoolType(),
            Block([If(BinaryOp('==',Id('k'),BooleanLiteral(True)),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_program_79(self):
        input = """
string isString(string str){if(s="ppl")return("p");else if(s="dsa")return("d");else return("nothing");}
                """
        expect=str(Program([FuncDecl(Id('isString'),[VarDecl('str',StringType())],StringType(),Block([If(BinaryOp('=',Id('s'),StringLiteral('ppl')),Return(StringLiteral('p')),
            If(BinaryOp('=',Id('s'),StringLiteral('dsa')),Return(StringLiteral('d')),Return(StringLiteral('nothing'))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_program_80(self):
        input = """
boolean isTrue(boolean k){if(k==true)return true;else return false;}
string isString(string str){if(s="ppl")return("p");else if(s="dsa")return("d");else return("nothing");}
void main(){int a; a = 1; printf(isTrue(a)||isString(a));}
                """
        expect=str(Program([FuncDecl(Id('isTrue'),[VarDecl('k',BoolType())],BoolType(),
            Block([If(BinaryOp('==',Id('k'),BooleanLiteral(True)),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),
            FuncDecl(Id('isString'),[VarDecl('str',StringType())],StringType(),
            Block([If(BinaryOp('=',Id('s'),StringLiteral('ppl')),Return(StringLiteral('p')),
            If(BinaryOp('=',Id('s'),StringLiteral('dsa')),Return(StringLiteral('d')),Return(StringLiteral('nothing'))))])),
            FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),
            BinaryOp('=',Id('a'),IntLiteral(1)),CallExpr(Id('printf'),[Id('isTrue'),BinaryOp('||',Id('a'),Id('isString')),Id('a')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_program_81(self):
        input = """
boolean isPrime;
int checkPrime(int index){for(i = 2; i <=index/2;i = i+1){if(index%i==0){return 0;}}return 1;}
                """
        expect=str(Program([VarDecl('isPrime',BoolType()),FuncDecl(Id('checkPrime'),[VarDecl('index',IntType())],IntType(),
            Block([For(BinaryOp('=',Id('i'),IntLiteral(2)),BinaryOp('<=',Id('i'),BinaryOp('/',Id('index'),IntLiteral(2))),
            BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([If(BinaryOp('==',BinaryOp('%',Id('index'),Id('i')),IntLiteral(0)),
            Block([Return(IntLiteral(0))]))])),Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test_program_82(self):
        input = """
boolean isTrue(boolean k){if(k==true)return true;else return false;}
string isString(string str){if(s="ppl")return("p");else if(s="dsa")return("d");else return("nothing");}
boolean isPrime;
int checkPrime(int index){for(i = 2; i <=index/2;i = i+1){if(index%i==0){return 0;}}return 1;}
void main(){int a; a = 1; printf(isTrue(a)||isString(a)||checkPrime(3));}
                """
        expect=str(Program([FuncDecl(Id('isTrue'),[VarDecl('k',BoolType())],BoolType(),
            Block([If(BinaryOp('==',Id('k'),BooleanLiteral(True)),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),
            FuncDecl(Id('isString'),[VarDecl('str',StringType())],StringType(),
            Block([If(BinaryOp('=',Id('s'),StringLiteral('ppl')),Return(StringLiteral('p')),
            If(BinaryOp('=',Id('s'),StringLiteral('dsa')),Return(StringLiteral('d')),Return(StringLiteral('nothing'))))])),
            VarDecl('isPrime',BoolType()),FuncDecl(Id('checkPrime'),[VarDecl('index',IntType())],IntType(),
            Block([For(BinaryOp('=',Id('i'),IntLiteral(2)),BinaryOp('<=',Id('i'),BinaryOp('/',Id('index'),IntLiteral(2))),
            BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([If(BinaryOp('==',BinaryOp('%',Id('index'),Id('i')),IntLiteral(0)),
            Block([Return(IntLiteral(0))]))])),Return(IntLiteral(1))])),
            FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),IntLiteral(1)),
            CallExpr(Id('printf'),[Id('isTrue'),BinaryOp('||',Id('a'),Id('isString')),BinaryOp('||',Id('a'),Id('checkPrime')),IntLiteral(3)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_program_83(self):
        input = """
int a[5];
void init(){for(i=0;i<5;i=i+1)a[i]=i;}
                """
        expect=str(Program([VarDecl('a',ArrayType(5,IntType())),FuncDecl(Id('init'),[],VoidType(),
        Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(5)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
        BinaryOp('=',ArrayCell(Id('a'),Id('i')),Id('i')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_program_84(self):
        input = """
int a[5];
void init(){for(i=0;i<5;i=i+1)a[i]=i;}
int main(int argc, string argv){init();for(i=0;i<5;i=i+1){printf(" : ",a[i]);}}
                """
        expect=str(Program([VarDecl('a',ArrayType(5,IntType())),FuncDecl(Id('init'),[],VoidType(),
        Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(5)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
        BinaryOp('=',ArrayCell(Id('a'),Id('i')),Id('i')))])),FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',StringType())],IntType(),
        Block([CallExpr(Id('init'),[]),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(5)),
        BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([CallExpr(Id('printf'),[StringLiteral(' : '),ArrayCell(Id('a'),Id('i'))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_if_statement_85 (self):
        input = """
                int main(){}
                int func(int a){
                    if (a) 
                        if (b)
                            if (c)
                                a;
                            else 
                                d;
                        else
                            c;
                    else 
                        e;
                }
                """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([])),
            FuncDecl(Id('func'),[VarDecl('a',IntType())],IntType(),Block([If(Id('a'),If(Id('b'),If(Id('c'),Id('a'),Id('d')),Id('c')),Id('e'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_type_86(self):
        input = """
int a,b[0],c[1],d[2];
float e[3],f[4];
boolean gh[5],j[100];
string s;
void ax(int a,int c,int d){
    foo(a,b,c,d,e,f,gh,j,s);
}
                """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',ArrayType(0,IntType())),VarDecl('c',ArrayType(1,IntType())),
        VarDecl('d',ArrayType(2,IntType())),VarDecl('e',ArrayType(3,FloatType())),VarDecl('f',ArrayType(4,FloatType())),
        VarDecl('gh',ArrayType(5,BoolType())),VarDecl('j',ArrayType(100,BoolType())),VarDecl('s',StringType()),FuncDecl(Id('ax'),
        [VarDecl('a',IntType()),VarDecl('c',IntType()),VarDecl('d',IntType())],VoidType(),Block([CallExpr(Id('foo'),
        [Id('a'),Id('b'),Id('c'),Id('d'),Id('e'),Id('f'),Id('gh'),Id('j'),Id('s')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_more_complex_program_87(self):
        input = """
int a;
float doubleThing(int a){
    if (a != 1)
        return a*a;
    else 
        return 1;
    do {
        "nothing in here";
        //this is nothing in here
    }while(exp);
}
                """
        expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('doubleThing'),[VarDecl('a',IntType())],FloatType(),
        Block([If(BinaryOp('!=',Id('a'),IntLiteral(1)),Return(BinaryOp('*',Id('a'),Id('a'))),Return(IntLiteral(1))),
        Dowhile([Block([StringLiteral('nothing in here')])],Id('exp'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_more_complex_program_88(self):
        input = """
void printf(string s[]){
    if (s != "") 
        printf("%s",s);
    else 
        return;
}
int main(){
    int a;
    scanf("%d",a);
    printf(a);
    printf("Hello World !");
}
                """
        expect = str(Program([FuncDecl(Id('printf'),[VarDecl('s',ArrayPointerType(StringType()))],VoidType(),
        Block([If(BinaryOp('!=',Id('s'),StringLiteral('')),CallExpr(Id('printf'),[StringLiteral('%s'),Id('s')]),Return())])),
        FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),CallExpr(Id('scanf'),[StringLiteral("""%d"""),Id('a')]),
        CallExpr(Id('printf'),[Id('a')]),CallExpr(Id('printf'),[StringLiteral('Hello World !')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_program_89(self):
        input = """
int main(int argc, string argv){printf("\\b\\t\\r",a[i]);}
                """
        expect= str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',StringType())],IntType(),
        Block([CallExpr(Id('printf'),[StringLiteral('\\b\\t\\r'),ArrayCell(Id('a'),Id('i'))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test_program_90(self):
        input = """
int main(int argc, string argv){printf("\\b\\t\\r\\n %d : ",a[i]);}
                """
        expect=str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',StringType())],IntType(),
        Block([CallExpr(Id('printf'),[StringLiteral('\\b\\t\\r\\n %d : '),ArrayCell(Id('a'),Id('i'))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_program_91(self):
        input = """
int main(int argc, string argv){printf(\"\\b\\t\\r %d :\",argc);}
                """
        expect=str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',StringType())],IntType(),
        Block([CallExpr(Id('printf'),[StringLiteral('\\b\\t\\r %d :'),Id('argc')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test_program_92(self):
        input = """
int main(int argc, string argv){printf("//this is line comment");}
                """
        expect= str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',StringType())],IntType(),Block([CallExpr(Id('printf'),[StringLiteral('//this is line comment')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test_program_93(self):
        input = """
int main(int argc, string argv){printf("this is line comment"/*this is block*/);}
                """
        expect=str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',StringType())],IntType(),
        Block([CallExpr(Id('printf'),[StringLiteral('this is line comment')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test_program_94(self):
        input = """
int main(int argc, string argv){printf("@~$%&';:[]_+");}//@~$%&';:\\[]_+);}
                """
        expect=str(Program([FuncDecl(Id('main'),[VarDecl('argc',IntType()),VarDecl('argv',StringType())],IntType(),Block([CallExpr(Id('printf'),[StringLiteral('@~$%&\';:[]_+')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_program_95(self):
        input = """
int gcd(int n1,int n2){for(i =1;i<=n1 && i<=n2;i=i+1){if(n1%i=0&&n2%i==0)return(i);}}
int main(){int n1,n2;printf("Enter : ");scanf("%d %d",n1,n2);printf(gcd(n1,n2));}
                """
        expect=str(Program([FuncDecl(Id('gcd'),[VarDecl('n1',IntType()),VarDecl('n2',IntType())],IntType(),
        Block([For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('&&',BinaryOp('<=',Id('i'),Id('n1')),BinaryOp('<=',Id('i'),Id('n2'))),
        BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
        Block([If(BinaryOp('=',BinaryOp('%',Id('n1'),Id('i')),BinaryOp('&&',IntLiteral(0),BinaryOp('==',BinaryOp('%',Id('n2'),Id('i')),IntLiteral(0)))),
        Return(Id('i')))]))])),FuncDecl(Id('main'),[],IntType(),Block([VarDecl('n1',IntType()),VarDecl('n2',IntType()),CallExpr(Id('printf'),
        [StringLiteral('Enter : ')]),CallExpr(Id('scanf'),[StringLiteral('%d %d'),Id('n1'),Id('n2')]),CallExpr(Id('printf'),[CallExpr(Id('gcd'),[Id('n1'),Id('n2')])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test_program_96(self):
        input = """
void reverseInt(int a){do{remainder = n%10;reverNum=reverNum*10+remainder;n=n/10;}while(a!=0);}
int main(){int n;printf("Enter : ");scanf("%d %d",n);reverseInt(a);printf(reverNum);}
                """
        expect=str(Program([FuncDecl(Id('reverseInt'),[VarDecl('a',IntType())],VoidType(),
        Block([Dowhile([Block([BinaryOp('=',Id('remainder'),BinaryOp('%',Id('n'),IntLiteral(10))),
        BinaryOp('=',Id('reverNum'),BinaryOp('+',BinaryOp('*',Id('reverNum'),IntLiteral(10)),Id('remainder'))),
        BinaryOp('=',Id('n'),BinaryOp('/',Id('n'),IntLiteral(10)))])],
        BinaryOp('!=',Id('a'),IntLiteral(0)))])),FuncDecl(Id('main'),[],IntType(),
        Block([VarDecl('n',IntType()),CallExpr(Id('printf'),[StringLiteral('Enter : ')]),CallExpr(Id('scanf'),[StringLiteral('%d %d'),Id('n')]),
        CallExpr(Id('reverseInt'),[Id('a')]),CallExpr(Id('printf'),[Id('reverNum')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_program_97(self):
        input = """
void dispFactor(int num){for(i=1;i<=num;i=i+1)if(num%i==0)printf("%d",i);}
int main(){int n;printf("Enter : ");scanf("%d %d",n);dispFactor(n);}
                """
        expect=str(Program([FuncDecl(Id('dispFactor'),[VarDecl('num',IntType())],VoidType(),
        Block([For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('<=',Id('i'),Id('num')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
        If(BinaryOp('==',BinaryOp('%',Id('num'),Id('i')),IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral('%d'),Id('i')])))])),
        FuncDecl(Id('main'),[],IntType(),Block([VarDecl('n',IntType()),CallExpr(Id('printf'),[StringLiteral('Enter : ')]),
        CallExpr(Id('scanf'),[StringLiteral('%d %d'),Id('n')]),CallExpr(Id('dispFactor'),[Id('n')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_program_98(self):
        input = """
int main(){for(i=0;i<n;i=i+1){scanf("%f",a[i]);}for(i=1;i<n;i=i+1){if(a[0]<a[i])a[0]=a[i];}printf("%f",a[0]);}
                """
        expect=str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),
        BinaryOp('<',Id('i'),Id('n')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
        Block([CallExpr(Id('scanf'),[StringLiteral('%f'),ArrayCell(Id('a'),Id('i'))])])),
        For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('<',Id('i'),Id('n')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
        Block([If(BinaryOp('<',ArrayCell(Id('a'),IntLiteral(0)),ArrayCell(Id('a'),Id('i'))),BinaryOp('=',ArrayCell(Id('a'),IntLiteral(0)),
        ArrayCell(Id('a'),Id('i'))))])),CallExpr(Id('printf'),[StringLiteral('%f'),ArrayCell(Id('a'),IntLiteral(0))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test_program_99(self):
        input = """
int power(int base, int powerRaised)
{
    if (powerRaised != 0)
        return (base*power(base, powerRaised-1));
    else
        return 1;
}
int main()
{
    int base, powerRaised, result;
    printf("Enter base number: ");
    scanf("%d",base);
    printf("Enter power number(positive integer): ");
    scanf("%d",powerRaised);
    result = power(base, powerRaised);
    printf("%d^%d = %d", base, powerRaised, result);
    return 0;
}
                """
        expect=str(Program([FuncDecl(Id('power'),[VarDecl('base',IntType()),VarDecl('powerRaised',IntType())],IntType(),
        Block([If(BinaryOp('!=',Id('powerRaised'),IntLiteral(0)),Return(BinaryOp('*',Id('base'),CallExpr(Id('power'),
        [Id('base'),BinaryOp('-',Id('powerRaised'),IntLiteral('1'))]))),Return(IntLiteral(1)))])),
        FuncDecl(Id('main'),[],IntType(),Block([VarDecl('base',IntType()),VarDecl('powerRaised',IntType()),VarDecl('result',IntType()),
        CallExpr(Id('printf'),[StringLiteral('Enter base number: ')]),CallExpr(Id('scanf'),[StringLiteral('%d'),Id('base')]),
        CallExpr(Id('printf'),[StringLiteral('Enter power number(positive integer): ')]),CallExpr(Id('scanf'),
        [StringLiteral('%d'),Id('powerRaised')]),BinaryOp('=',Id('result'),CallExpr(Id('power'),[Id('base'),Id('powerRaised')])),
        CallExpr(Id('printf'),[StringLiteral('%d^%d = %d'),Id('base'),Id('powerRaised'),Id('result')]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))