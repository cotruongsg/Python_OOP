import random
class WordFinder:
    def __init__(self, path):
        txt = open(path,'r')
        self.words = self.parse(txt)
        print(f'{len(self.words)} words read')

    def parse(self,txt):
        return [w.strip() for w in txt]

    def random(self):
        return random.choice(self.words)

w = WordFinder('Exercises\Python\OOP\simple.txt')
print(w.random())
print(w.random())
print(w.random())

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    def parse(self, txt):
        return [w.strip() for w in txt if w.strip() and not w.startswith('#')]

spec = SpecialWordFinder('Exercises\Python\OOP\complex.txt')
print(spec.random())

