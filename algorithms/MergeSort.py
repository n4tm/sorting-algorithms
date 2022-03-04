from utils.ISortingAlgorithm import ISortingAlgorithm

class MergeSort(ISortingAlgorithm):
  def sort(self, data: list[int]) -> None:
    n = len(data)
    if n <= 1:
      return
    # Finding the mid of the array
    mid = n//2
    # Dividing the array elements into 2 halves
    L, R = data[:mid], data[mid:]
    # Sorting the first half
    self.sort(L)
    # Sorting the second half
    self.sort(R)

    i = j = k = 0
    # Copy data to temporary lists L[] and R[]
    lLength, rLength = len(L), len(R) 
    while i < lLength and j < rLength:
      if L[i] < R[j]:
        data[k] = L[i]
        i += 1
      else:
        data[k] = R[j]
        j += 1
      k += 1
    # Checking if any element was left
    while i < lLength:
      data[k] = L[i]
      i += 1
      k += 1
    while j < rLength:
      data[k] = R[j]
      j += 1
      k += 1