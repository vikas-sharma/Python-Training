import doc_ex

print(dir(doc_ex)) # display programs, functions under doc_ex file

print(__name__)
print(__file__)
print(__doc__)
print(__cached__)
print(__package__)
print(__loader__)
print(__spec__)


print(help(doc_ex))
print(help(doc_ex.func))