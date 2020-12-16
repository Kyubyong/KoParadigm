# KoParadigm: A Korean Conjugation Paradigm Generator

This is the offical repo for our paper: [KoParadigm: A Korean Conjugation Paradigm Generator](https://arxiv.org/abs/2004.13221)

(Inflectional) paradigm means the set of all the inflected forms of a word. For example, English verb "look" has inflected forms like "look", "look-s", "look-ed", and "look-ing", as all of you know.
 Paradigms are widely used in corpus linguistics or search engines.
To create the full paradigm set of a language is sometimes tricky. It is particularly so when we deal with a morphologically rich language like Korean.
Inflection of Korean verbs is notorisouly complicated. Typically, a Korean verb can combine with more than 100 endings. What is worse, the combination rules are not simple at all.
 They are determined by the sound of the verb/ending, and the part-of-speech of the verb (action / descriptive). That's why so far there's no open sources of Korean paradigm generator, I think.
 Here's the first one. With KoParadigm, you can easily get the full paradigm of a Korean verb. 
 
## Dependencies
* python >=3.6
* jamo >=0.4.1
* xlrd == 1.2.0

## Installation
```
pip install koparadigm
```

## Usage
```
>>> from koparadigm import Paradigm, prettify
>>> p = Paradigm()
>>> verb = "곱" # Note that you must drop the final ending 다
>>> paradigms = p.conjugate(verb) # this returns list of lists
>>> print(paradigms)
[['Action Verb', [('거나', '곱거나'), ('거늘', '곱거늘'), ('거니', '곱거니') ...]]]
>>> prettify(paradigms)
POS = Action Verb
• ending = 거나 form = 곱거나
• ending = 거늘 form = 곱거늘
• ending = 거니 form = 곱거니
...
==================== 2 ====================
POS = Descriptive Verb
• ending = 거나 form = 곱거나
• ending = 거늘 form = 곱거늘
• ending = 거니 form = 곱거니
• ending = 거니와 form = 곱거니와
...

```
## References
If you use our software for research, please cite:

```
@article{park2020KoParadigm,
  author = {Park, Kyubyong },
  title={KoParadigm: A Korean Conjugation Paradigm Generator},
  journal={arXiv preprint arXiv:2004.13221},
  year={2020}
}
```
