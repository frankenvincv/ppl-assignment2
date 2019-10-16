# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u0186\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\6\2q\n\2\r\2\16")
        buf.write("\2r\3\3\6\3v\n\3\r\3\16\3w\3\3\3\3\7\3|\n\3\f\3\16\3\177")
        buf.write("\13\3\3\3\5\3\u0082\n\3\5\3\u0084\n\3\3\3\7\3\u0087\n")
        buf.write("\3\f\3\16\3\u008a\13\3\3\3\3\3\6\3\u008e\n\3\r\3\16\3")
        buf.write("\u008f\3\3\5\3\u0093\n\3\3\3\6\3\u0096\n\3\r\3\16\3\u0097")
        buf.write("\3\3\3\3\5\3\u009c\n\3\3\4\3\4\3\5\3\5\5\5\u00a2\n\5\3")
        buf.write("\5\6\5\u00a5\n\5\r\5\16\5\u00a6\3\6\3\6\7\6\u00ab\n\6")
        buf.write("\f\6\16\6\u00ae\13\6\3\6\3\6\3\6\3\7\3\7\5\7\u00b5\n\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\5\32\u0114\n\32\3\32\3\32\3\32\7\32\u0119\n\32\f")
        buf.write("\32\16\32\u011c\13\32\3\33\3\33\3\33\3\33\7\33\u0122\n")
        buf.write("\33\f\33\16\33\u0125\13\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\34\7\34\u0130\n\34\f\34\16\34\u0133\13")
        buf.write("\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3")
        buf.write("!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\6\64\u016c")
        buf.write("\n\64\r\64\16\64\u016d\3\64\3\64\3\65\3\65\7\65\u0174")
        buf.write("\n\65\f\65\16\65\u0177\13\65\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\7\67\u017f\n\67\f\67\16\67\u0182\13\67\3\67\3\67")
        buf.write("\3\67\3\u0123\28\3\3\5\4\7\2\t\2\13\5\r\2\17\2\21\6\23")
        buf.write("\7\25\b\27\t\31\n\33\13\35\f\37\r!\16#\17%\20\'\21)\22")
        buf.write("+\23-\24/\2\61\2\63\25\65\26\67\279\30;\31=\32?\33A\34")
        buf.write("C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61")
        buf.write("m\62\3\2\t\4\2GGgg\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttv")
        buf.write("v\4\2C\\c|\3\2\62;\4\2\f\f\17\17\5\2\13\f\17\17\"\"\2")
        buf.write("\u0198\2\3\3\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3p\3\2\2\2\5\u009b\3\2\2")
        buf.write("\2\7\u009d\3\2\2\2\t\u009f\3\2\2\2\13\u00a8\3\2\2\2\r")
        buf.write("\u00b4\3\2\2\2\17\u00b6\3\2\2\2\21\u00b9\3\2\2\2\23\u00c1")
        buf.write("\3\2\2\2\25\u00c7\3\2\2\2\27\u00d0\3\2\2\2\31\u00d5\3")
        buf.write("\2\2\2\33\u00d9\3\2\2\2\35\u00df\3\2\2\2\37\u00e2\3\2")
        buf.write("\2\2!\u00e6\3\2\2\2#\u00ed\3\2\2\2%\u00f2\3\2\2\2\'\u00f5")
        buf.write("\3\2\2\2)\u00fb\3\2\2\2+\u0100\3\2\2\2-\u0106\3\2\2\2")
        buf.write("/\u010d\3\2\2\2\61\u010f\3\2\2\2\63\u0113\3\2\2\2\65\u011d")
        buf.write("\3\2\2\2\67\u012b\3\2\2\29\u0136\3\2\2\2;\u0138\3\2\2")
        buf.write("\2=\u013a\3\2\2\2?\u013c\3\2\2\2A\u013e\3\2\2\2C\u0140")
        buf.write("\3\2\2\2E\u0142\3\2\2\2G\u0145\3\2\2\2I\u0148\3\2\2\2")
        buf.write("K\u014a\3\2\2\2M\u014d\3\2\2\2O\u0150\3\2\2\2Q\u0153\3")
        buf.write("\2\2\2S\u0156\3\2\2\2U\u0158\3\2\2\2W\u015a\3\2\2\2Y\u015c")
        buf.write("\3\2\2\2[\u015e\3\2\2\2]\u0160\3\2\2\2_\u0162\3\2\2\2")
        buf.write("a\u0164\3\2\2\2c\u0166\3\2\2\2e\u0168\3\2\2\2g\u016b\3")
        buf.write("\2\2\2i\u0171\3\2\2\2k\u0178\3\2\2\2m\u017a\3\2\2\2oq")
        buf.write("\5\61\31\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\4")
        buf.write("\3\2\2\2tv\5\61\31\2ut\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3")
        buf.write("\2\2\2xy\3\2\2\2y\u0083\5\7\4\2z|\5\61\31\2{z\3\2\2\2")
        buf.write("|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0084\3\2\2\2\177}")
        buf.write("\3\2\2\2\u0080\u0082\5\t\5\2\u0081\u0080\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083}\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0084\u009c\3\2\2\2\u0085\u0087\5\61\31")
        buf.write("\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008b\u008d\5\7\4\2\u008c\u008e\5\61\31")
        buf.write("\2\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\3\2\2\2\u0091")
        buf.write("\u0093\5\t\5\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\u009c\3\2\2\2\u0094\u0096\5\61\31\2\u0095\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\5\t\5\2")
        buf.write("\u009a\u009c\3\2\2\2\u009bu\3\2\2\2\u009b\u0088\3\2\2")
        buf.write("\2\u009b\u0095\3\2\2\2\u009c\6\3\2\2\2\u009d\u009e\7\60")
        buf.write("\2\2\u009e\b\3\2\2\2\u009f\u00a1\t\2\2\2\u00a0\u00a2\5")
        buf.write(";\36\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4")
        buf.write("\3\2\2\2\u00a3\u00a5\5\61\31\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\n\3\2\2\2\u00a8\u00ac\7$\2\2\u00a9\u00ab\5\r\7")
        buf.write("\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00af\u00b0\7$\2\2\u00b0\u00b1\b\6\2\2")
        buf.write("\u00b1\f\3\2\2\2\u00b2\u00b5\n\3\2\2\u00b3\u00b5\5\17")
        buf.write("\b\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\16")
        buf.write("\3\2\2\2\u00b6\u00b7\7^\2\2\u00b7\u00b8\t\4\2\2\u00b8")
        buf.write("\20\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7q\2\2\u00bb")
        buf.write("\u00bc\7q\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\u00bf\7c\2\2\u00bf\u00c0\7p\2\2\u00c0\22\3\2\2\2\u00c1")
        buf.write("\u00c2\7d\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4\7g\2\2\u00c4")
        buf.write("\u00c5\7c\2\2\u00c5\u00c6\7m\2\2\u00c6\24\3\2\2\2\u00c7")
        buf.write("\u00c8\7e\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca\7p\2\2\u00ca")
        buf.write("\u00cb\7v\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd")
        buf.write("\u00ce\7w\2\2\u00ce\u00cf\7g\2\2\u00cf\26\3\2\2\2\u00d0")
        buf.write("\u00d1\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3")
        buf.write("\u00d4\7g\2\2\u00d4\30\3\2\2\2\u00d5\u00d6\7h\2\2\u00d6")
        buf.write("\u00d7\7q\2\2\u00d7\u00d8\7t\2\2\u00d8\32\3\2\2\2\u00d9")
        buf.write("\u00da\7h\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7q\2\2\u00dc")
        buf.write("\u00dd\7c\2\2\u00dd\u00de\7v\2\2\u00de\34\3\2\2\2\u00df")
        buf.write("\u00e0\7k\2\2\u00e0\u00e1\7h\2\2\u00e1\36\3\2\2\2\u00e2")
        buf.write("\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7v\2\2\u00e5")
        buf.write(" \3\2\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("\u00e9\7v\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb\7t\2\2\u00eb")
        buf.write("\u00ec\7p\2\2\u00ec\"\3\2\2\2\u00ed\u00ee\7x\2\2\u00ee")
        buf.write("\u00ef\7q\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7f\2\2\u00f1")
        buf.write("$\3\2\2\2\u00f2\u00f3\7f\2\2\u00f3\u00f4\7q\2\2\u00f4")
        buf.write("&\3\2\2\2\u00f5\u00f6\7y\2\2\u00f6\u00f7\7j\2\2\u00f7")
        buf.write("\u00f8\7k\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa\7g\2\2\u00fa")
        buf.write("(\3\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd")
        buf.write("\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff*\3\2\2\2\u0100")
        buf.write("\u0101\7h\2\2\u0101\u0102\7c\2\2\u0102\u0103\7n\2\2\u0103")
        buf.write("\u0104\7u\2\2\u0104\u0105\7g\2\2\u0105,\3\2\2\2\u0106")
        buf.write("\u0107\7u\2\2\u0107\u0108\7v\2\2\u0108\u0109\7t\2\2\u0109")
        buf.write("\u010a\7k\2\2\u010a\u010b\7p\2\2\u010b\u010c\7i\2\2\u010c")
        buf.write(".\3\2\2\2\u010d\u010e\t\5\2\2\u010e\60\3\2\2\2\u010f\u0110")
        buf.write("\t\6\2\2\u0110\62\3\2\2\2\u0111\u0114\5/\30\2\u0112\u0114")
        buf.write("\7a\2\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114")
        buf.write("\u011a\3\2\2\2\u0115\u0119\5/\30\2\u0116\u0119\5\61\31")
        buf.write("\2\u0117\u0119\7a\2\2\u0118\u0115\3\2\2\2\u0118\u0116")
        buf.write("\3\2\2\2\u0118\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\64\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011d\u011e\7\61\2\2\u011e\u011f\7,\2\2")
        buf.write("\u011f\u0123\3\2\2\2\u0120\u0122\13\2\2\2\u0121\u0120")
        buf.write("\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0124\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0126\u0127\7,\2\2\u0127\u0128\7\61\2\2\u0128\u0129\3")
        buf.write("\2\2\2\u0129\u012a\b\33\3\2\u012a\66\3\2\2\2\u012b\u012c")
        buf.write("\7\61\2\2\u012c\u012d\7\61\2\2\u012d\u0131\3\2\2\2\u012e")
        buf.write("\u0130\n\7\2\2\u012f\u012e\3\2\2\2\u0130\u0133\3\2\2\2")
        buf.write("\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\3")
        buf.write("\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\b\34\3\2\u0135")
        buf.write("8\3\2\2\2\u0136\u0137\7-\2\2\u0137:\3\2\2\2\u0138\u0139")
        buf.write("\7/\2\2\u0139<\3\2\2\2\u013a\u013b\7,\2\2\u013b>\3\2\2")
        buf.write("\2\u013c\u013d\7\61\2\2\u013d@\3\2\2\2\u013e\u013f\7\'")
        buf.write("\2\2\u013fB\3\2\2\2\u0140\u0141\7#\2\2\u0141D\3\2\2\2")
        buf.write("\u0142\u0143\7~\2\2\u0143\u0144\7~\2\2\u0144F\3\2\2\2")
        buf.write("\u0145\u0146\7(\2\2\u0146\u0147\7(\2\2\u0147H\3\2\2\2")
        buf.write("\u0148\u0149\7?\2\2\u0149J\3\2\2\2\u014a\u014b\7>\2\2")
        buf.write("\u014b\u014c\7?\2\2\u014cL\3\2\2\2\u014d\u014e\7@\2\2")
        buf.write("\u014e\u014f\7?\2\2\u014fN\3\2\2\2\u0150\u0151\7#\2\2")
        buf.write("\u0151\u0152\7?\2\2\u0152P\3\2\2\2\u0153\u0154\7?\2\2")
        buf.write("\u0154\u0155\7?\2\2\u0155R\3\2\2\2\u0156\u0157\7>\2\2")
        buf.write("\u0157T\3\2\2\2\u0158\u0159\7@\2\2\u0159V\3\2\2\2\u015a")
        buf.write("\u015b\7]\2\2\u015bX\3\2\2\2\u015c\u015d\7_\2\2\u015d")
        buf.write("Z\3\2\2\2\u015e\u015f\7*\2\2\u015f\\\3\2\2\2\u0160\u0161")
        buf.write("\7+\2\2\u0161^\3\2\2\2\u0162\u0163\7}\2\2\u0163`\3\2\2")
        buf.write("\2\u0164\u0165\7\177\2\2\u0165b\3\2\2\2\u0166\u0167\7")
        buf.write("=\2\2\u0167d\3\2\2\2\u0168\u0169\7.\2\2\u0169f\3\2\2\2")
        buf.write("\u016a\u016c\t\b\2\2\u016b\u016a\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f")
        buf.write("\3\2\2\2\u016f\u0170\b\64\3\2\u0170h\3\2\2\2\u0171\u0175")
        buf.write("\7$\2\2\u0172\u0174\5\r\7\2\u0173\u0172\3\2\2\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176j\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\13\2\2")
        buf.write("\2\u0179l\3\2\2\2\u017a\u0180\7$\2\2\u017b\u017f\n\3\2")
        buf.write("\2\u017c\u017d\7^\2\2\u017d\u017f\n\4\2\2\u017e\u017b")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0182\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0183\u0184\7$\2\2\u0184\u0185\b")
        buf.write("\67\4\2\u0185n\3\2\2\2\32\2rw}\u0081\u0083\u0088\u008f")
        buf.write("\u0092\u0097\u009b\u00a1\u00a6\u00ac\u00b4\u0113\u0118")
        buf.write("\u011a\u0123\u0131\u016d\u0175\u017e\u0180\5\3\6\2\b\2")
        buf.write("\2\3\67\3")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    STRINGLIT = 3
    BOOLEAN = 4
    BREAK = 5
    CONTINUE = 6
    ELSE = 7
    FOR = 8
    FLOAT = 9
    IF = 10
    INT = 11
    RETURN = 12
    VOID = 13
    DO = 14
    WHILE = 15
    TRUE = 16
    FALSE = 17
    STRING = 18
    ID = 19
    BlockComment = 20
    LineComment = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    OR = 28
    AND = 29
    ASSIGN = 30
    LTE = 31
    GTE = 32
    NEQ = 33
    EQ = 34
    LT = 35
    GT = 36
    LSB = 37
    RSB = 38
    LB = 39
    RB = 40
    LP = 41
    RP = 42
    SEMI = 43
    COMA = 44
    WS = 45
    UNCLOSE_STRING = 46
    ERROR_CHAR = 47
    ILLEGAL_ESCAPE = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'continue'", "'else'", "'for'", "'float'", 
            "'if'", "'int'", "'return'", "'void'", "'do'", "'while'", "'true'", 
            "'false'", "'string'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'||'", "'&&'", "'='", "'<='", "'>='", "'!='", "'=='", "'<'", 
            "'>'", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "STRINGLIT", "BOOLEAN", "BREAK", "CONTINUE", 
            "ELSE", "FOR", "FLOAT", "IF", "INT", "RETURN", "VOID", "DO", 
            "WHILE", "TRUE", "FALSE", "STRING", "ID", "BlockComment", "LineComment", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "OR", "AND", "ASSIGN", 
            "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "LSB", "RSB", "LB", "RB", 
            "LP", "RP", "SEMI", "COMA", "WS", "UNCLOSE_STRING", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTLIT", "FLOATLIT", "Dot", "Exponent", "STRINGLIT", 
                  "STR_CHAR", "ESC_SEQ", "BOOLEAN", "BREAK", "CONTINUE", 
                  "ELSE", "FOR", "FLOAT", "IF", "INT", "RETURN", "VOID", 
                  "DO", "WHILE", "TRUE", "FALSE", "STRING", "Letter", "Digit", 
                  "ID", "BlockComment", "LineComment", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "OR", "AND", "ASSIGN", "LTE", "GTE", 
                  "NEQ", "EQ", "LT", "GT", "LSB", "RSB", "LB", "RB", "LP", 
                  "RP", "SEMI", "COMA", "WS", "UNCLOSE_STRING", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text[1:]);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.STRINGLIT_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    self.text = y[1:-1]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    position = self.text.find("\\")
                    y = str(self.text)
                    self.text = y[1:position + 2]
                
     


