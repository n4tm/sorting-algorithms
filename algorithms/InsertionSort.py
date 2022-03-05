from utils.SortingAlgorithm import SortingAlgorithm

class InsertionSort(SortingAlgorithm):
  def sort(self, data: list[int]) -> None:
    # Traverse through 1 to len(data)
    for i in range(1, len(data)):
      element = data[i]
      # Move elements of [0..i-1], that are
      # greater than current element, to one position ahead
      # of their current position
      j = i-1
      while j >= 0 and element < data[j]:
        data[j + 1] = data[j]
        j -= 1
      data[j + 1] = element