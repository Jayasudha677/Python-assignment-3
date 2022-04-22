from audioop import reverse

from mysqlx import ProgrammingError


def rev_words(string):
    words = string.split(' ')
    rev = ' '.join(reversed(words))
    return rev
s="Python ProgrammingError"
print("reverse:",rev_words(s))
s2="javascript html"
print("reverse:",rev_words(s2))