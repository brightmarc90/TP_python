class IterNumber:
    
    def __init__(self, coef, numbers):
        self.coef = coef
        self.numbers = numbers
        self.index = 0 

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index] * self.coef
            self.index += 1
            return result
        else:
            raise StopIteration

values = IterNumber(coef = .01, numbers = [91, 11, 100, 3938])

# On itère sur la classe IterNumber
for e in values:
    print(e)