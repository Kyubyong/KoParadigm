from koparadigm import Paradigm, prettify
p = Paradigm()
verb = "곱"
paradigms = p.conjugate(verb)
print(paradigms)
prettify(paradigms)