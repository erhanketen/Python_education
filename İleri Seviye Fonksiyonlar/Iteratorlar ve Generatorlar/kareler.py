class Kareler:
    def __init__(self, maksimum):
        self.maksimum = maksimum
        self.sayac = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.sayac += 1
        if self.sayac <= self.maksimum:
            return self.sayac ** 2

        else:
            self.sayac = 0
            raise StopIteration


kare = Kareler(maksimum=10)

for i in kare:
    print(i)







