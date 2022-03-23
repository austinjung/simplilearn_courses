from matplotlib import pylab

from nltk.text import Text
from nltk.app.chartparser_app import CFG, ChartParserApp
from nltk.app.rdparser_app import RecursiveDescentApp
from nltk import parse, CFG

grammar = CFG.fromstring(
    """
    # # Grammatical productions.
    #     S -> NP VP
    #     VP -> VP PP | V NP | V
    #     NP -> Det N | NP PP
    #     PP -> P NP
    # # Lexical productions.
    #     NP -> 'John' | 'I'
    #     Det -> 'the' | 'my' | 'a'
    #     N -> 'dog' | 'cookie' | 'table' | 'cake' | 'fork'
    #     V -> 'ate' | 'saw'
    #     P -> 'on' | 'under' | 'with'

    # Grammatical productions.
        S -> NP VP | VP | NP
        VP -> VP PP | V5 NP NP | V3 NP | V1 ADJ | V3 | V1
        ADVP -> ADV1 ADV1 | ADV1
        ADJP -> ADVP ADJP | ADJ
        NP -> Det ADJP NP | ADJP N | Det N | NP PP | N
        PP -> P NP | ADV2
    # Lexical productions.
        NP -> 'John' | 'I' | 'the table'
        Det -> 'the' | 'my' | 'a'
        N -> 'dog' | 'cookie' | 'table' | 'cake' | 'fork'
        ADV1 -> 'very'
        ADJ -> 'beautiful'
        V3 -> 'ate' | 'saw'
        P -> 'on' | 'under' | 'with'

    """
)

# sent = "John ate the cake on the table with a fork"
sent = "John saw a very beautiful dog on the table"
tokens = list(sent.split())
# tokens = ['John', 'ate', 'the', 'cake', 'on', 'the table', 'with', 'a', 'fork']

# print("grammar= (")
# for rule in grammar.productions():
#     print(("    ", repr(rule) + ","))
# print(")")
print("tokens = %r" % tokens)
# print('Calling "ChartParser(grammar).parse(tokens)"...')
parser = parse.ChartParser(grammar)
ps = list(parser.parse(tokens))
for p in parser.parse(tokens):
    print(p)

#
# grammar = CFG.fromstring(
#     """
#     S -> NP VP
#     NP -> Det N | Det N PP
#     VP -> V NP | V NP PP
#     PP -> P NP
#     NP -> 'I'
#     N -> 'man' | 'park' | 'telescope' | 'dog'
#     Det -> 'the' | 'a'
#     P -> 'in' | 'with'
#     V -> 'saw'
#     """
# )
#
# sent = "I saw a man in the park"
# tokens = list(sent.split())
#
# print("grammar= (")
# for rule in grammar.productions():
#     print(("    ", repr(rule) + ","))
# print(")")
# print("tokens = %r" % tokens)
# print('Calling "RecursiveDescent(grammar).parse(tokens)"...')
# parser = parse.RecursiveDescentParser(grammar, trace=0)
# for p in parser.parse(tokens):
#     print(p)
