from utils.SortingAlgorithm import SortingAlgorithm

class BubbleSort(SortingAlgorithm):
  def sort(self, data: list[int]) -> None:
    n = len(data)
    # Traverse through all elements
    for i in range(n-1):
      # Last i elements are already in place (guaranteed)
      # traverse the array from 0 to n-i-1
      for j in range(n-i-1):
        # Swap if the element found is greater
        if data[j] > data[j + 1]:
          data[j], data[j + 1] = data[j + 1], data[j]