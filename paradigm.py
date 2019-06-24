from rules import *
from collections import OrderedDict


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
                ending2forms = OrderedDict()
                rules = self.verb_label2rules[verb_label]
                for ending_label, rule in rules:
                    endings = self.label2endings[ending_label]
                    for ending in endings:
                        forms = inflect(verb, ending, rule)
                        if forms == []:
                            forms = "N/A"
                        else:
                            forms = "/".join(forms)
                        ending2forms[ending] = forms
                ret.append(ending2forms)
            return ret
        else:
            print(f"{verb} is not in the dictionary.")
