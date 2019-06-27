from collections import OrderedDict

from koparadigm.rules import *


class Paradigm(object):
    def __init__(self):
        self.verb2labels = verb2labels()
        self.verb_label2rules = verb_label2rules()
        self.label2endings = label2endings()

    def __call__(self, verb):
        if verb in self.verb2labels:
            ret = []
            verb_labels = self.verb2labels[verb]
            for verb_label in verb_labels:
                print(verb_label)
                # pos
                if verb_label < 27:
                    pos = "동사"
                elif verb_label in (27, 28):
                    pos = "동사/형용사"
                elif verb_label < 55:
                    pos = "형용사"
                else:
                    pos = "조사"
                # ending info.
                ending2forms = OrderedDict()
                rules = self.verb_label2rules[verb_label]
                for ending_label, rule in rules:
                    endings = self.label2endings[ending_label]
                    for ending in endings:
                        forms = inflect(verb, ending, rule)
                        if len(forms)==0: continue
                        forms = "/".join(forms)

                        ending2forms[ending] = forms

                ret.append([pos, ending2forms])
            return ret
        else:
            print(f"{verb} is not in the dictionary.")
