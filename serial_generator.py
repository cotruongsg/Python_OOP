class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start) :
        self.start = start  

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.start} + 1>"     

    def generate(self):       
        self.start += 1
        return self.start  - 1

    def reset(self):
        self.start = 100

gen = SerialGenerator(start=100)
print(gen.generate())
print(gen.generate())
print(gen.generate())
print(gen.generate())
print(gen.generate())
print(gen.generate())
print(gen.generate())
print(gen.generate())
print(gen.generate())
print(gen.generate())
gen.reset()
print(gen.generate())
print(gen.generate())
print(gen.generate())
print(gen.generate())
