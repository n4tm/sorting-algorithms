from utils.ISortingAlgorithm import ISortingAlgorithm

class SelectionSort(ISortingAlgorithm):
  def sort(self, data: list[int]) -> None:
    # Traverse through all array elements
    for i in range(len(data)):
      # Find the minimum element index
      minElementIndex = i
      for j in range(i+1, len(data)):
        if data[minElementIndex] > data[j]:
          minElementIndex = j
      # Swap the found minimum element with the first element        
      data[i], data[minElementIndex] = data[minElementIndex], data[i]