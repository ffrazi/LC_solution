class NumberContainers:

    def __init__(self):
        self.numbers=collections.defaultdict(SortedSet)
        self.index_numbers={}

    def change(self, index: int, number: int) -> None:
        if index in self.index_numbers:
            oldnumber=self.index_numbers[index]
            self.numbers[oldnumber].remove(index)
            if not self.numbers[oldnumber]:
                del self.numbers[oldnumber]
        self.index_numbers[index]=number
        self.numbers[number].add(index)


    def find(self, number: int) -> int:
        if number in self.numbers and self.numbers[number]:
            return self.numbers[number][0]
        return -1
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)