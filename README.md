# KoParadigm: Korean Inflectional Paradigm Generator

(Inflectional) paradigm means the set of all the inflected forms of a word. For example, English verb "look" has inflected forms like "look", "look-s", "look-ed", and "look-ing", as all of you know.
 Paradigms are widely used in corpus linguistics or search engines.
To create the full paradigm set of a language is sometimes tricky. It is particularly so when we deal with a morphologically rich language like Korean.
Inflection of Korean verbs is notorisouly complicated. Typically, a Korean verb can combine with more than 100 endings. What is worse, the combination rules are not simple at all.
 They are determined by the sound of the verb/ending, and the part-of-speech of the verb (action / descriptive). That's why so far there's no open sources of Korean paradigm generator, I think.
 Here's the first one. With KoParadigm, you can easily get the full paradigm of a Korean verb. 
 
## Dependencies
* python >=3.6
* jamo >=0.4.1
* xlrd > 1.2.0

## Installation
```
pip install koparadigm
```

## Usage
```
>>> from koparadigm import Paradigm
>>> p = Paradigm()

>>> verb = "곱" # Note that you must drop the final ending 다
>>> paradigms = p(verb) # this returns list of lists
>>> print(paradigms)
[['동사', OrderedDict([('는다', '곱는다'), ('는다고', '곱는다고'), ('는다나', '곱는다나'), ('는다네', '곱는다네'), ('는다더라', '곱는다더라'), ('는다느니', '곱는다느니'), ('는다마는', '곱는다마는'), ('는다손', '곱는다손'), ('는담', '곱는담'), ('는답시고', '곱는답시고') ...
['형용사', OrderedDict([('습네', '곱습네'), ('습늰다', '곱습늰다'), ('습니까', '곱습니까'), ('습니다', '곱습니다'), ('습디까', '곱습디까'), ('습디다', '곱습디다'), ('습딘다', '곱습딘다'), ('습지요', '곱습지요'), ('으나', '고우나') ...]]
>>> for paradigm in paradigms:
...     print("pos =", paradigm[0])
...     for ending, form in paradigm[1].items():
...         print("ending =", ending, "form =", form)
...     print()
pos = 동사
ending = 는다 form = 곱는다
ending = 는다고 form = 곱는다고
ending = 는다나 form = 곱는다나
...

pos = 형용사
ending = 습네 form = 곱습네
ending = 습늰다 form = 곱습늰다
ending = 습니까 form = 곱습니까
...

```
## References
If you use our software for research, please cite:

```
@misc{KoParadigm2019,
  author = {Park, Kyubyong },
  title = {KoParadigm},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Kyubyong/paradigm}}
}
```