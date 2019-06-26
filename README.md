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
pip install Koparadigm
```

## Usage
```
from koparadigm import Paradigm
p = Paradigm()

verb = "먹" # Note that you must drop the final ending 다
paradigms = p(verb) # this returns list due to homographs
for paradigm in paradigms:
    print(paradigm)
>> OrderedDict([('는다', '먹는다'), ('는다고', '먹는다고'), ('는다나', '먹는다나'), ('는다네', '먹는다네'), ('는다더라', '먹는다더라'), ('는다느니', '먹는다느니'), ('는다마는',  '먹는다마는'), ('으라고', '먹으라고'), ('으락', '먹으락'), ('으랴', '먹으랴'), ('으러', '먹으러'), ('으려', '먹으려'), 
('아야만', 'N/A'), ('아야지', 'N/A'), ('아요', 'N/A'), ...

# The keys and values of the dictioary are endings and forms, respectively.
# N/A denotes that the verb does NOT combine with the ending.

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