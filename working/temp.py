import xlrd
from glob import glob
import re

with open('verb2', 'w', encoding='utf8') as fout:
    lines = set()
    for line in open('verb', 'r', encoding='utf8'):
        lines.add(line)
    lines = sorted(list(lines))
    fout.write("".join(lines))


# def do(word, ending, pos, num_v, num_a):
#     if word.endswith(ending):
#         if pos == "동사":
#             if num_v == "": return None
#             c = word + "\t" + f"{num_v}\n"
#             return c
#         elif pos=="형용사":
#             if num_a == "": return None
#             c = word + "\t" + f"{num_a}\n"
#             return c
#     return None
#
# files = glob("/Users/ryan/git/old_hangul/urimalsam/*")
# with open('verb', 'w', encoding='utf8') as fout:
#     words = set()
#     for f in files:
#         book = xlrd.open_workbook(f)
#
#
#         sh = book.sheet_by_index(0)
#         for rx in range(1, sh.nrows):
#             row = sh.row(rx)
#             if re.search("[^\-ㄱ-힣]", row[0].value) is not None: continue
#             word = re.sub("[^ㄱ-힣]", "", row[0].value)
#             pos = row[11].value
#
#             c = do(word, "하다", pos, 26, 52)
#             if c is not None:
#                 words.add(c)
#                 continue
#
#             c = do(word, "되다", pos, 21, 47)
#             if c is not None:
#                 words.add(c)
#                 continue
#
#             c = do(word, "받다", pos, 1, "")
#             if c is not None:
#                 words.add(c)
#                 continue
#
#             c = do(word, "시키다", pos, 19, "")
#             if c is not None:
#                 words.add(c)
#                 continue
#
#             c = do(word, "드리다", pos, 19, "")
#             if c is not None:
#                 words.add(c)
#                 continue
#
#             c = do(word, "거리다", pos, 19, "")
#             if c is not None:
#                 words.add(c)
#                 continue
#
#             c = do(word, "대다", pos, 20, "")
#             if c is not None:
#                 words.add(c)
#                 continue
#
#             c = do(word, "스럽다", pos, "", 34)
#             if c is not None:
#                 words.add(c)
#                 continue
#             #
#             #
#             # if pos == "동사":
#             #     c = word + "\t" + "26\n"
#             #     words.add(c)
#             #     # fout.write()
#             # elif pos == "형용사":
#             #     c = word +" \t" + "52\n"
#             #     words.add(c)
#             #     # fout.write(word +" \t" + "52\n")
#
#     words = sorted(list(words))
#     fout.write("".join(words))