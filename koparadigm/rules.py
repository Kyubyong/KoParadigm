import xlrd
from jamo import h2j, j2h, hcj_to_jamo, is_hcj
import re
import os

book = xlrd.open_workbook(os.path.dirname(os.path.abspath(__file__)) + "/paradigm.xlsx")


def verb2labels():
    d = dict()
    sh = book.sheet_by_name("verbs")
    for rx in range(1, sh.nrows):
        verb = sh.row(rx)[0].value
        label = int(sh.row(rx)[1].value)
        if verb in d:
            if label not in d[verb]:
                d[verb].append(label)
        else:
            d[verb] = [label]

    return d


def verb_label2rules():
    d = dict()
    sh = book.sheet_by_name("rules")
    ending_labels = sh.row(0)
    for rx in range(2, sh.nrows):
        # print(sh.row(rx)[0].value)
        verb_label = int(sh.row(rx)[0].value)
        for i, ending_label in enumerate(ending_labels):
            if i in (0,1): continue
            ending_label = int(ending_label.value)
            rule = sh.row(rx)[i].value
            if verb_label in d:
                d[verb_label].append((ending_label, rule))
            else:
                d[verb_label]= [(ending_label, rule)]

    return d


def label2endings():
    d = dict()
    sh = book.sheet_by_name("endings")
    for rx in range(1, sh.nrows):
        ending = sh.row(rx)[0].value
        label = int(sh.row(rx)[1].value)
        if label in d:
            if ending not in d[label]:
                d[label].append(ending)
        else:
            d[label] = [ending]

    return d


def j2syl(string):
    choseong = "[\u1100-\u1112]"
    jungseong = "[\u1161-\u1175]"
    jongseong = "[\u11A8-\u11C2]"
    
    # CVC
    matches = re.findall(f"{choseong}{jungseong}{jongseong}", string)
    for match in matches:
        syl = j2h(*match)
        string = string.replace(match, syl)
        
    # CV
    matches = re.findall(f"{choseong}{jungseong}", string)
    for match in matches:
        syl = j2h(*match)
        string = string.replace(match, syl)
        
    return string


def inflect(verb, ending, rule):
    if not rule:
        return []
    verb = h2j(verb)
    ending = h2j(ending)
    ending = "".join(hcj_to_jamo(char, "tail") if is_hcj(char) else char for char in ending )
    rules = rule[1:-1].split("/")
    forms = []
    for rule in rules:
        end, insertion, start = rule.split(",")

        end = int(end) if not end=="" else 100
        start = int(start) if not start=="" else 0
        form = verb[:end] + insertion + ending[start:]
        form = j2syl(form)
        forms.append(form)
    return forms


