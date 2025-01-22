from typing import List


class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self) -> List:
        """Sorts the array using Insertion Sort."""
        for i in range(1, len(self.array)):
            self.insert(i)
        return self.array

    def insert(self, i):
        """Inserts the 'Transition element' into its correct position in the sorted portion of the array."""
    #     TODO: TO BE IMPLEMENTED
        current_value = self.array[i]
        position = i
        while position > 0 and self.array[position - 1] > current_value:
            self.array[position] = self.array[position - 1]
            position -= 1
        self.array[position] = current_value

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
